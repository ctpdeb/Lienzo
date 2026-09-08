// Lienzo — shared site behavior (menu overlay, active nav state, scroll reveal)

(function () {
  // Mark the current page's nav link active (top tabs)
  var here = (location.pathname.split('/').pop() || 'index.html');
  document.querySelectorAll('.top-tabs a').forEach(function (a) {
    var target = a.getAttribute('href');
    if (target === here || (here === '' && target === 'index.html')) {
      a.classList.add('active');
    }
  });

  // Subtle scroll-reveal, respects prefers-reduced-motion via the .reveal CSS itself
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  // Keep the story controls in sync with the horizontal snap viewer.
  var viewer = document.querySelector('.story-viewer');
  if (viewer) {
    var slides = Array.prototype.slice.call(viewer.querySelectorAll('.story-slide'));
    var count = document.querySelector('.story-count');
    var updateCount = function () {
      var nearest = 0;
      var smallestDistance = Infinity;
      slides.forEach(function (slide, index) {
        var distance = Math.abs(slide.getBoundingClientRect().left - viewer.getBoundingClientRect().left);
        if (distance < smallestDistance) {
          smallestDistance = distance;
          nearest = index;
        }
      });
      if (count) count.textContent = 'Slide ' + (nearest + 1) + ' of ' + slides.length;
    };
    var moveTo = function (offset) {
      var current = Math.round(viewer.scrollLeft / (slides[0].offsetWidth + 18));
      var next = Math.max(0, Math.min(slides.length - 1, current + offset));
      slides[next].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
      window.setTimeout(updateCount, 350);
    };
    var previous = document.querySelector('.story-prev');
    var next = document.querySelector('.story-next');
    if (previous) previous.addEventListener('click', function () { moveTo(-1); });
    if (next) next.addEventListener('click', function () { moveTo(1); });
    viewer.addEventListener('scroll', updateCount, { passive: true });
    updateCount();
  }
})();

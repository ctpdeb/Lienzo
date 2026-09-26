// Lienzo — scroll reveal and the StereoEEG story viewer.
(function () {
  document.documentElement.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Reveal on scroll
  var reveals = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  }

  // Home hero: gentle scroll parallax, and the brain tilts toward the pointer
  var hero = document.querySelector(".hero-stars");
  if (hero && !reduce) {
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var y = Math.min(window.scrollY, window.innerHeight);
        hero.style.setProperty("--sy", y.toFixed(0));
        ticking = false;
      });
    }, { passive: true });

    var tilt = hero.querySelector(".tilt");
    if (tilt && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
      hero.addEventListener("pointermove", function (e) {
        var r = hero.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        tilt.style.transform = "perspective(900px) rotateY(" + (x * 8).toFixed(2) + "deg) rotateX(" + (-y * 6).toFixed(2) + "deg)";
      });
      hero.addEventListener("pointerleave", function () { tilt.style.transform = ""; });
    }
  }

  // StereoEEG story viewer
  var viewer = document.querySelector("[data-viewer]");
  if (viewer) {
    var slides = viewer.querySelectorAll(".stage img");
    var thumbs = viewer.querySelectorAll(".thumbs button");
    var count = viewer.querySelector(".count");
    var caption = viewer.querySelector(".stage-caption");
    var i = 0;
    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("on", k === i); });
      thumbs.forEach(function (b, k) { b.setAttribute("aria-current", k === i ? "true" : "false"); });
      count.textContent = "Page " + (i + 1) + " of " + slides.length;
      caption.textContent = slides[i].alt;
    }
    viewer.querySelector("[data-prev]").addEventListener("click", function () { show(i - 1); });
    viewer.querySelector("[data-next]").addEventListener("click", function () { show(i + 1); });
    thumbs.forEach(function (b, k) { b.addEventListener("click", function () { show(k); }); });
    viewer.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") { show(i - 1); e.preventDefault(); }
      if (e.key === "ArrowRight") { show(i + 1); e.preventDefault(); }
    });
    // Exhibition frames jump to their page in the viewer
    document.querySelectorAll("[data-goto]").forEach(function (f) {
      f.addEventListener("click", function () {
        show(+f.dataset.goto);
        document.getElementById("story").scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
        viewer.querySelector("[data-next]").focus({ preventScroll: true });
      });
    });
    show(0);
  }
})();

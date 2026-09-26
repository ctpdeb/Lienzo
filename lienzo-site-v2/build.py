#!/usr/bin/env python3
"""Regenerates the six HTML pages (shared header, nav and footer). Run: python3 build.py"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "ctp.deborah@gmail.com"

MARK = ('<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
        '<rect x="4.5" y="4.5" width="23" height="23" rx="1"/>'
        '<path d="M9 21c2.5-5.5 5.5-9 8.5-7.5 2.6 1.3.2 5.4 2.8 5.9 1.6.3 2.6-1.2 3.2-2.4" stroke-linecap="round"/></svg>')
ARROW = ('<span class="arrow" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" '
         'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>')

NAV = [("index.html", "Home"), ("method.html", "Method"), ("pastworks.html", "Past works"),
       ("about.html", "About"), ("vision.html", "Vision")]
CTA = ("get-involved.html", "Get involved")

STORY = [
    ("page-01", "Welcome to Children's National"),
    ("page-02", "A child learning what a seizure is"),
    ("page-03", "A child learning about the stereoEEG procedure"),
    ("page-04", "Meeting the hospital care team in the pre-op area"),
    ("page-05", "A child receiving anesthesia before surgery"),
    ("page-06", "A robot helping the surgical team place wires"),
    ("page-07", "A child waking up with a bandage around their head"),
    ("page-08", "A child playing and spending time with family in the hospital"),
    ("page-09", "A nurse helping keep the child safe during the hospital stay"),
    ("page-10", "Therapy dogs visiting a child in the hospital"),
    ("page-11", "A child resting while the computer records seizure information"),
    ("page-12", "A brave brain explorer finishing their hospital journey"),
]


def cur(href, page):
    return ' aria-current="page"' if href == page else ""


def shell(page, title, desc, body, topbar_on_canvas=False):
    pill = "".join(f'<a href="{h}"{cur(h, page)}>{t}</a>' for h, t in NAV)
    pill += f'<a class="pill-cta" href="{CTA[0]}"{cur(CTA[0], page)}>{CTA[1]}</a>'
    foot_links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    tb = "topbar on-canvas" if topbar_on_canvas else "topbar"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#111844">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23111844'/%3E%3Crect x='7.5' y='7.5' width='17' height='17' fill='none' stroke='%23EAE0CF' stroke-width='1.8'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Public+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="{tb}">
  <a class="wordmark" href="index.html" aria-label="Lienzo, home">{MARK}Lienzo</a>
  <nav class="topnav" aria-label="Primary">{pill}</nav>
  <a class="btn btn-outline-light head-cta" href="mailto:{EMAIL}?subject=Lienzo">Email Deborah</a>
</header>

<main id="main">
{body}
</main>

<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="wordmark" href="index.html">{MARK}Lienzo</a>
        <p>Visual education for neurological care, founded by Deborah Torrico-Pardo in the Washington, D.C. area.</p>
      </div>
      <div><ul>{foot_links}<li><a href="{CTA[0]}">{CTA[1]}</a></li></ul></div>
      <div><p>Write to Deborah</p><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
    <div class="fine"><p>Lienzo materials are educational. They do not replace individualized medical advice.</p></div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def thumb(n):
    return f"assets/stereoeeg/thumbs/{STORY[n][0]}.jpg"


def full(n):
    return f"assets/stereoeeg/{STORY[n][0]}.jpg"


# ---------------------------------------------------------------- mosaic
# ---------------------------------------------------------------- pages

ANNOS = [  # (label, x%, y%, side) — points on the recoloured brain illustration
    ("Frontal lobe", 27, 38, "l"),
    ("Parietal lobe", 60, 27, "r"),
    ("Temporal lobe", 40, 56, "l"),
    ("Cerebellum", 66, 59, "r"),
    ("Brainstem", 58, 67, "l"),
]


def annos():
    return "\n        ".join(
        f'<span class="anno {side}" style="left:{x}%;top:{y}%;--i:{n}"><span class="dot"></span><span class="lbl">{t}</span></span>'
        for n, (t, x, y, side) in enumerate(ANNOS))


def words(text, first_block=True):
    """Wrap each word for the headline rise-in; the first letter gets the colour block."""
    out = []
    for n, w in enumerate(text.split()):
        inner = f'<span class="block">{w[0]}</span>{w[1:]}' if (n == 0 and first_block) else w
        out.append(f'<span class="w"><span style="--i:{n}">{inner}</span></span>')
    return " ".join(out)


def letters(word):
    return "".join(f'<span style="--i:{n}">{c}</span>' for n, c in enumerate(word))


HOME = f"""
<section class="hero-stars" aria-labelledby="home-title">
  <div class="stage-panel">
    <figure class="brain">
      <div class="tilt">
        <img src="assets/brain-blue.jpg" alt="Illustration of a human brain, shown from the side, in Lienzo blue" width="960" height="960">
        <div class="annos" aria-hidden="true">
          {annos()}
        </div>
      </div>
    </figure>
    <div class="hero-copy">
      <p class="kicker">Visual education for neurological care</p>
      <h1 id="home-title" class="rise">{words("Reimagining art as a language for understanding neurological care")}</h1>
      <p class="hero-lede">Lienzo transforms complex neurological procedures and diagnoses into clinically validated visual education that patients and families can actually understand.</p>
      <div class="cta-row">
        <a class="btn btn-dark" href="pastworks.html">See our first clinical application {ARROW}</a>
        <a class="btn btn-outline-dark" href="about.html">Meet the founder</a>
      </div>
    </div>
    <p class="ghost ghost-letters" aria-hidden="true">{letters("lienzo")}</p>
  </div>
</section>

<section class="section canvas" aria-labelledby="problem-title">
  <div class="wrap">
    <div class="problem-grid reveal">
      <div>
        <p class="kicker">The problem</p>
        <h2 id="problem-title" class="display h-lg">The stress of the unknown</h2>
      </div>
      <div class="body">
        <p>Major pediatric hospitals perform thousands of complex procedures each year. For families, entering this environment brings immense anxiety, especially when medical information is delivered in dense clinical terms or a language they do not speak.</p>
        <p>Many handouts also leave out the patient. Young patients and their siblings are often left confused, scared, and out of the loop of conversations about their own health. Complex medical descriptions create an unfair barrier, making high-quality care feel distant to children and inaccessible to families navigating it for the first time.</p>
      </div>
    </div>

    <div class="bridge-text reveal">
      <p class="kicker">The answer</p>
      <h2 class="display h-lg">Bridging the gap through pictures</h2>
      <p class="lede">Lienzo uses a universal language: art. By turning intricate medical steps into clear, intuitive visual guides, we give patients and families a clearer picture of their stay at the hospital.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="format-title">
  <div class="wrap">
    <div class="sec-head reveal">
      <div>
        <p class="kicker">What Lienzo makes</p>
        <h2 id="format-title" class="display h-lg">Neuroscience, translated.</h2>
      </div>
      <p>Three ways the same clinically reviewed artwork reaches families: a shared library, a hospital platform, and custom commissions.</p>
    </div>
    <div class="ledger">
      <div class="ledger-row reveal">
        <h3>Education Library</h3>
        <p><span class="who">For families and clinicians</span>A growing set of clinically reviewed visual guides and teaching stories, organized by condition and procedure.</p>
      </div>
      <div class="ledger-row reveal">
        <h3>Hospital Platform</h3>
        <p><span class="who">For hospitals and clinics</span>Printable, digital, and multilingual guides from the library, reviewed with each hospital's team and handed out as part of standard care.</p>
      </div>
      <div class="ledger-row reveal">
        <h3>Custom Studio</h3>
        <p><span class="who">For care teams</span>Hospitals commission Lienzo to build education specific to their own procedures and patient populations.</p>
      </div>
    </div>
    <p style="margin-top:40px" class="reveal"><a class="btn btn-outline-light" href="method.html">How each piece is made</a></p>
  </div>
</section>

<section class="canvas etym" aria-labelledby="name-title">
  <span class="ghost" aria-hidden="true">canvas</span>
  <div class="wrap">
    <div class="inner reveal">
      <div>
        <h2 id="name-title" class="entry-word" aria-label="lienzo"><span class="spell" aria-hidden="true">{letters("lienzo")}</span></h2>
        <p class="entry-meta"><i>noun, Spanish.</i> Canvas: the surface an illustration is built on, layer by layer.</p>
      </div>
      <div>
        <p class="lede">Families build understanding the same way during a health crisis, one layer at a time. The name comes from Deborah's first language, and it's an invitation to people from every background.</p>
        <a class="btn btn-light" href="about.html">Meet Deborah {ARROW}</a>
      </div>
    </div>
  </div>
</section>
"""

LAZY = ' loading="lazy"'


def slides():
    imgs = "\n          ".join(
        f'<img src="{full(i)}" alt="{a}" width="1188" height="918"{LAZY if i else ""}>' for i, (_, a) in enumerate(STORY))
    th = "\n          ".join(
        f'<button type="button" aria-label="Page {i+1}: {a}"><img src="{thumb(i)}" alt="" width="360" height="278" loading="lazy"></button>'
        for i, (_, a) in enumerate(STORY))
    return imgs, th


IMGS, THUMBS = slides()

PAST = f"""
<section class="expo" aria-labelledby="work-title">
  <div>
    <h1 id="work-title" class="title"><small>The Lienzo archive</small>Past works</h1>
    <p class="sub">Illustrated teaching stories, made with clinicians for the children and families they care for.</p>
    <a class="btn btn-light" href="#stereoeeg">See StereoEEG {ARROW}</a>
  </div>
</section>

<section class="section work" id="stereoeeg" aria-labelledby="story-title">
  <div class="wrap">
    <div class="work-head reveal">
      <div>
        <p class="kicker">Teaching story, made with Children's National</p>
        <h2 id="story-title" class="display h-xl">StereoEEG</h2>
      </div>
      <p class="lede">A child-friendly visual story that helps young patients understand what happens before, during, and after a stereoEEG procedure.</p>
    </div>
    <div class="viewer" id="story" data-viewer>
      <div>
        <div class="stage" tabindex="0" aria-roledescription="carousel" aria-label="StereoEEG story pages. Use the left and right arrow keys to turn pages.">
          {IMGS}
        </div>
        <div class="stage-bar">
          <span class="count" aria-live="polite">Page 1 of 12</span>
          <div class="ctrls">
            <button class="icon-btn" type="button" data-prev aria-label="Previous page"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 8H3M7 4L3 8l4 4"/></svg></button>
            <button class="icon-btn" type="button" data-next aria-label="Next page"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg></button>
          </div>
        </div>
        <p class="stage-caption">{STORY[0][1]}</p>
        <div class="thumbs">
          {THUMBS}
        </div>
      </div>
      <aside class="details" aria-label="Project details">
        <dl>
          <div class="row"><dt>Artist</dt><dd>Deborah Torrico-Pardo</dd></div>
          <div class="row"><dt>Collaborators</dt><dd>Heymann, Perrine</dd></div>
          <div class="row"><dt>Hospital</dt><dd>Children's National</dd></div>
          <div class="row"><dt>Format</dt><dd>Illustrated teaching story, 12 pages</dd></div>
          <div class="row"><dt>Made for</dt><dd>Young patients and their families</dd></div>
        </dl>
      </aside>
    </div>
  </div>
</section>

<section class="section canvas" aria-labelledby="proc-title">
  <div class="wrap">
    <div class="procedure reveal">
      <div>
        <p class="kicker">The procedure, briefly</p>
        <h2 id="proc-title" class="display h-md">What a stereoEEG is</h2>
      </div>
      <p>A stereoEEG helps doctors learn where seizures begin. While a child is asleep under anesthesia, the surgical team places thin wires in carefully chosen areas of the brain. The wires stay connected to a computer during a hospital stay so the care team can record seizure activity and use that information to plan the next step in care.</p>
    </div>
  </div>
</section>

<section class="section canvas-2" aria-labelledby="next-title">
  <div class="wrap">
    <div class="next-slot reveal">
      <div>
        <h2 id="next-title" class="display h-md">The next story is still a blank canvas</h2>
        <p>More works are on the way. If there's a procedure or diagnosis your families struggle to understand, it could be the next one.</p>
      </div>
      <a class="btn btn-light" href="get-involved.html">Suggest a procedure {ARROW}</a>
    </div>
  </div>
</section>
"""

ABOUT = f"""
<section class="about-page canvas" aria-labelledby="why-title">
  <div class="wrap about-grid">
    <div class="about-main">
      <p class="kicker">Why Lienzo exists</p>
      <h1 id="why-title" class="display h-lg">Art as a universal language</h1>
      <div class="body">
        <p>Lienzo is a health-literacy initiative built on a simple observation: the path from a clinical diagnosis to a family's real understanding is often blocked by stress, dense medical terminology, and a near-total absence of accessible visual aids.</p>
        <p>Coming from a minority background, Deborah experienced firsthand the barriers to navigating the medical system. Passionate about drawing and painting from a young age, she sees art as a universal language. Her mission is to harness creative expression, uplifting local artists to transform how medical information is shared and processed in hospital settings.</p>
        <p>Lienzo is the Spanish word for canvas, the foundation an illustration is built on, layer by layer, much like a family builds understanding during a health crisis. Rooted in Deborah's native language, the name grounds the brand in her own heritage and invites people from all backgrounds to learn the language of clinical care.</p>
      </div>
    </div>
    <aside class="me" aria-label="About Deborah">
      <img src="assets/deborah-portrait.jpg" alt="Portrait of Deborah Torrico-Pardo" width="900" height="861">
      <p class="hello">Hello, I'm</p>
      <h2 class="me-name"><span class="block">D</span>eborah Torrico-Pardo</h2>
      <p class="me-role">Founder of Lienzo. I'm building the visual layer of neurological care: neuroscience, illustration, and a belief that medicine should be taught in a language every family already speaks, pictures and stories.</p>
      <dl class="me-facts">
        <div><dt>Background</dt><dd>Neuroscience, illustration, and healthcare exposure</dd></div>
        <div><dt>First product</dt><dd>StereoEEG Family Education Kit</dd></div>
        <div><dt>Based in</dt><dd>Washington, D.C. metro area</dd></div>
        <div><dt>Contact</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      </dl>
      <a class="btn btn-light" href="pastworks.html">See the StereoEEG story {ARROW}</a>
    </aside>
  </div>
</section>
"""

STEPS = [
    ("Identify", "Interview clinicians and families to surface real pain points."),
    ("Map", "Pinpoint exactly where misunderstanding happens."),
    ("Translate", "Convert the concept into visual language."),
    ("Validate", "Clinician review for clinical accuracy."),
    ("Pilot", "Test with the families it's made for."),
    ("Measure", "Track comprehension, confidence, and recall."),
    ("Deploy", "Distribute through hospitals and clinics."),
    ("Iterate", "Real feedback shapes the next version."),
]

METHOD = f"""
<section class="method-hero" aria-labelledby="method-title">
  <div class="panel">
    <div class="title-cell">
      <p class="kicker">Built with clinicians</p>
      <h1 id="method-title">The Lienzo Method</h1>
    </div>
    <p class="panel-lede">A repeatable product-development pipeline, so accuracy and effectiveness are provable, not just claimed.</p>
    <p class="ghost" aria-hidden="true">método</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(64px,9vw,120px)" aria-labelledby="steps-title">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2 id="steps-title" class="display h-lg">Eight steps, every time</h2>
      <p>Each guide moves from a clinician's real pain point to a validated, distributed piece of artwork, and then back again with feedback.</p>
    </div>
    <ol class="steps">
      {"".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in STEPS)}
    </ol>
  </div>
</section>

<section class="section canvas" aria-labelledby="serve-title">
  <div class="wrap">
    <div class="sec-head reveal">
      <div>
        <p class="kicker">Who Lienzo serves</p>
        <h2 id="serve-title" class="display h-lg">Three customers, three roles</h2>
      </div>
    </div>
    <div class="roles">
      <div class="role-row reveal"><span class="tag">Payer</span><h3>Hospitals and clinics</h3><p>Commission custom content and distribute it to patients as part of standard care.</p></div>
      <div class="role-row reveal"><span class="tag">Channel and validation</span><h3>Clinicians</h3><p>The distribution channel and clinical validation network. A neurologist who wants this in every family's hands pulls it into the workflow.</p></div>
      <div class="role-row reveal"><span class="tag">End user</span><h3>Families</h3><p>Free basic guides today; a premium layer of personalized preparation and interactive modules once the institutional model is proven.</p></div>
    </div>
    <p style="margin-top:44px" class="reveal"><a class="btn btn-light" href="get-involved.html">Become a clinical advisor {ARROW}</a></p>
  </div>
</section>
"""

VISION = f"""
<section class="vision-hero" aria-labelledby="vision-title">
  <div class="wrap">
    <p class="kicker">Where this goes</p>
    <h1 id="vision-title" class="display h-xl">The visual layer of neurological care</h1>
  </div>
</section>

<section class="section" style="padding-top:40px" aria-label="Timeline">
  <div class="wrap">
    <ol class="horizon">
      <li class="reveal"><span class="when">Today</span><div><h2>StereoEEG</h2><p>One procedure, developed with families in mind and ready to be clinically piloted.</p></div></li>
      <li class="reveal"><span class="when">Tomorrow</span><div><h2>Epilepsy, neurodevelopment, brain tumors</h2><p>The same method, applied condition by condition, building a real content library.</p></div></li>
      <li class="reveal"><span class="when">Eventually</span><div><h2>A universal visual language for medicine</h2><p>Clinical expertise, a content library, validation data, and institutional relationships, compounding into the standard for how neurological care is explained.</p></div></li>
    </ol>
  </div>
</section>

<section class="section canvas" aria-labelledby="settings-title">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2 id="settings-title" class="display h-md">Where Lienzo belongs</h2>
      <p>The care settings where families meet complex neurological procedures most often.</p>
    </div>
    <ul class="settings reveal">
      <li>Pediatric epilepsy programs</li>
      <li>Children's hospitals</li>
      <li>Developmental pediatric clinics</li>
      <li>School-based health programs</li>
    </ul>
  </div>
</section>
"""

MAILTO_ADVISOR = f"mailto:{EMAIL}?subject=Lienzo%20clinical%20advisor"
MAILTO_ARTIST = f"mailto:{EMAIL}?subject=Making%20materials%20with%20Lienzo"
MAILTO_HOSPITAL = f"mailto:{EMAIL}?subject=Lienzo%20hospital%20partnership"

INVOLVE = f"""
<section class="involve-hero" aria-labelledby="inv-title">
  <div class="wrap">
    <p class="kicker">Get involved</p>
    <h1 id="inv-title" class="display h-xl">Make neurological care easier to understand</h1>
    <p class="lede" style="margin-top:28px">Lienzo works with people who can bring a story to life, and institutions that want families to feel more prepared.</p>
    <div class="paths">
      <div class="path reveal">
        <p class="who">For clinicians</p>
        <h2>Advise a story</h2>
        <p>Tell us where families get stuck. One short call and a round or two of feedback by email.</p>
        <a class="btn btn-light" href="#advisor">What we ask {ARROW}</a>
      </div>
      <div class="path reveal">
        <p class="who">For students and artists</p>
        <h2>Make materials</h2>
        <p>Illustration, animation, design, writing, translation, or helping shape patient education.</p>
        <a class="btn btn-outline-light" href="{MAILTO_ARTIST}">Write to Deborah</a>
      </div>
      <div class="path reveal">
        <p class="who">For hospitals</p>
        <h2>Bring Lienzo to your families</h2>
        <p>Share your team, patient population, and the procedure or diagnosis you want to make clearer.</p>
        <a class="btn btn-outline-light" href="{MAILTO_HOSPITAL}">Discuss a partnership</a>
      </div>
    </div>
  </div>
</section>

<section class="section canvas" id="advisor" aria-labelledby="adv-title">
  <div class="wrap">
    <div class="advisor">
      <div class="reveal">
        <p class="kicker">For clinicians</p>
        <h2 id="adv-title" class="pull">Built with, not for.</h2>
        <p class="lede">Every Lienzo resource exists because a clinician told us exactly where families get stuck. The advisory role stays light: one short call, one or two rounds of feedback by email, nothing more.</p>
        <p style="margin-top:28px"><a class="btn btn-light" href="{MAILTO_ADVISOR}">Request an intro call {ARROW}</a></p>
      </div>
      <ol class="asks reveal">
        <li><div><h3>Initial discovery <span class="time">15 minutes</span></h3><p>A brief call or email to name the two or three concepts you most wish you had a handout for in clinic.</p></div></li>
        <li><div><h3>Review by email</h3><p>Look over one or two visual drafts. Your clinical edits go directly into the artwork.</p></div></li>
        <li><div><h3>Recognition</h3><p>Advisors and their institutions are credited on all distributed materials, digital portfolios, and public health exhibitions.</p></div></li>
      </ol>
    </div>
  </div>
</section>
"""

PAGES = [
    ("index.html", "Lienzo | Visual education for neurological care",
     "Lienzo turns complex neurological procedures into clinically validated visual education that children and families can understand.", HOME, False),
    ("method.html", "The Lienzo Method", "The eight-step, clinician-built process behind every Lienzo guide.", METHOD, False),
    ("pastworks.html", "Past works | Lienzo", "Lienzo's past works, starting with StereoEEG, a teaching story made with Children's National.", PAST, False),
    ("about.html", "About Deborah | Lienzo", "Why Lienzo exists, and Deborah Torrico-Pardo, its founder.", ABOUT, False),
    ("vision.html", "Vision | Lienzo", "Where Lienzo goes next.", VISION, False),
    ("get-involved.html", "Get involved | Lienzo", "Advise, make materials, or bring Lienzo to your hospital.", INVOLVE, False),
]

for fn, title, desc, body, oc in PAGES:
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(shell(fn, title, desc, body, oc))
print("built", len(PAGES), "pages")

# Lienzo — build notes

This is a plain static site: HTML + CSS + a little vanilla JS, no build step, no framework. Open `index.html` in a browser or run a local server (see below) and it just works. Meant to be dropped straight into VS Code.

## Structure

```
lienzo-site/
  index.html          Home
  method.html          The Lienzo Method + three customers + advisor program
  stereoeeg.html        StereoEEG Family Education Kit (the MVP)
  founder.html          About Deborah + the origin story
  vision.html           Today / tomorrow / eventually + target care settings
  contact.html          Contact
  css/style.css         Everything visual lives here
  js/main.js             Menu overlay, active-nav highlighting, scroll reveal
  assets/deborah-portrait.jpg   Founder photo (duotone-treated via CSS, not the raw file)
  NOTES.md              This file
```

Each page is a full, independent HTML file with its own copy of the header/nav/footer markup. There's no templating — if you change the nav (add a page, rename a link), you have to update it in all six files. That's a deliberate simplicity tradeoff for a 6-page site; if this grows past ~10 pages, it's worth moving to a static site generator (11ty, Astro) or a simple build script that injects shared partials.

## Running it locally

No build step needed, but opening `index.html` directly from disk (`file://`) will work for layout/content, though some browsers restrict a few things over `file://`. Easiest to serve it locally:

```
cd lienzo-site
python3 -m http.server 8000
# then open http://localhost:8000
```

or with Node: `npx serve .`

## Design system (in `css/style.css`)

- **Palette** (CSS custom properties at the top of the file): `--navy` #111844, `--indigo` #4B5694, `--dusty` #7288AE, `--cream` #EAE0CF, plus `--cream-raised` for card surfaces. Change these four values to re-theme the whole site.
- **Type**: "Instrument Serif" for headlines (loaded from Google Fonts — swap the `<link>` tag in every page's `<head>` if you change it), "Public Sans" for body/UI text. Both are loaded via the same Google Fonts `<link>` at the top of each page.
- **Components**: `.btn` / `.btn-solid` / `.btn-ghost` / `.btn-on-navy` / `.btn-ghost-on-navy` cover the button variants used on light vs. navy backgrounds. `.card`, `.catalog-row`, `.role-line`, `.tl-row` are the recurring list/row patterns — deliberately not 3-column card grids, see below.
- **Layout choice**: content is presented as flowing numbered lists/ledgers (the Method pipeline, the three customer roles, the vision timeline) rather than even card grids, to avoid the generic "3-card row" template look. If you want a grid back for any of these, the CSS classes are self-contained enough to swap without touching markup structure much.

## Navigation

The nav is a full-screen "index" overlay (navy background, big serif numbered links) triggered by the circle menu button, top right, on every page. This was a deliberate fix: the previous single-file version hid nav links entirely on narrow screens with no way to reach them — this overlay works at every screen size and is the primary nav now, not just a mobile fallback. `js/main.js` handles opening/closing it (click, the × button, or Escape) and highlights whichever page you're currently on.

## Known gaps / things to decide before this goes live publicly

- **Contact info**: only `ctp.deborah@gmail.com` is on the site right now. A personal phone number was in earlier drafts and has been deliberately removed — decide if you want a dedicated business email/phone before sharing this widely, since anything here is public once shared.
- **No real contact form** — the "Talk to us" / advisor CTAs are all `mailto:` links. Fine for now; add a form (e.g. via Formspree, or a backend) if you want submissions tracked.
- **Claims about traction**: copy has been kept to what you've actually told me happened (a coloring book you made, used informally) rather than implying a formal clinical pilot. If a real pilot happens, update the StereoEEG and Vision pages to say so specifically (which hospital, how many families, what was measured) — specific numbers are far more credible than "piloted with families."
- **Children's National / any real institution**: intentionally not named or logo'd anywhere on the site since there's no confirmed partnership yet (see the Vision page's "target care settings," which names institution *types*, not specific organizations). Update this the moment a real pilot is signed.
- **Founder photo**: treated with a CSS grayscale + navy color-blend duotone effect (in `founder.html`'s `.photo-panel` styling) rather than swapping in a new edited image file — if you'd rather have a literally re-edited photo, that's a Photoshop/Figma step outside this codebase.
- **SEO/social**: only basic `<title>` and meta description are set per page. No Open Graph image, no favicon yet — add a favicon file and reference it in each page's `<head>` if you want one.

## To adjust content

All copy is plain HTML in each page file — no CMS, no data file. Search for the text you want to change directly in the relevant `.html` file and edit in place.

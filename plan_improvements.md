# Proposed Improvements for Vikas's Reports

## 1. Interactive Tag/Category Filter on the Homepage
Since the site now has 12 reports ranging across Economics, History, Geopolitics, and Country-specific profiles, finding relevant reports is becoming harder.
- **Implementation**: Add a sleek row of clickable tags above the grid (e.g., `All`, `Economics`, `Geopolitics`, `Asia`, `History`). Clicking a tag instantly filters the grid using CSS/JS.
- **Vibe**: Smooth fade animations when filtering.

## 2. Reading Time & Progress Meta Data at the Top of Reports
We added the reading progress bar (the gold line at the top of the window), but the reports themselves just dive straight into the text.
- **Implementation**: Inject a small, elegant "meta bar" right beneath the title on every report page:
  `Written by Vikas Gaur • March 2026 • ⏳ 45 min read`
- **Vibe**: Makes the essays feel like premium Substack or Atlantic articles.

## 3. Custom Favicon
Currently the browser tab just shows a generic globe icon.
- **Implementation**: Create a base64 encoded golden `VG` favicon (matching the About Avatar) and inject it into all HTML pages via `enhancements.js`. 
- **Vibe**: Instant brand recognition; makes the site look finished.

## 4. "Share this Report" floating buttons
Readers might want to share these incredible long-form pieces on WhatsApp or Twitter/X.
- **Implementation**: A highly minimal, sticky vertical bar on the left side (or bottom on mobile) with subtle icons for Twitter, WhatsApp, and "Copy Link".
- **Vibe**: Encourages organic growth without looking spammy.

## 5. Subtle "Scroll Reveal" Animations
Currently, when you open the homepage, everything is just *there*.
- **Implementation**: Add a very lightweight `IntersectionObserver` script to `enhancements.js` (or `index.html`) so that as the user scrolls down the homepage, the report cards softly fade and slide up into view.
- **Vibe**: High-end editorial sites (like NYT interactive or Apple) use this to make the page feel "alive".

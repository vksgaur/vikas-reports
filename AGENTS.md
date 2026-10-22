# AGENTS.md — Global Context & Agent Guidelines for Vikas Gaur

## 1. Identity & Operating Principles
* **User:** Vikas Gaur
* **Mission:** Cultivate a personal ecosystem of knowledge, deep-dive research reports, an interconnected digital garden, and a personal blog.
* **Core Rule for the Agent:** Minimize technical friction. Vikas wants to focus on reading, thinking, and writing. Handle technical configurations, build scripts, deployment pipelines, and git plumbing cleanly behind the scenes.

---

## 2. Voice, Tone & Writing Style Guidelines
Whenever generating essays, reports, blog posts, or garden notes for Vikas, strictly adhere to these rules:
1. **The Tradition:** Write in the tradition of **Yuval Noah Harari** (*Sapiens*) combined with **Ramachandra Guha** and **Barbara Tuchman**.
2. **Clarity & Accessibility:** Serious narrative journalism written for an intelligent, intellectually hungry Indian reader who has no formal academic background in the subject.
3. **No Academic Hedging or Jargon:** Never use dense theoretical jargon or passive academic hedging. Explain profound ideas over a long, thoughtful evening conversation with a friend.
4. **Grounded in Concrete Reality:** Every abstract concept or economic principle must be grounded in a specific person, a concrete moment, or a tangible place.
5. **Dual Truths (No Blind Celebration):** Never let narratives become uncritical celebrations of power or progress. The same rationalism that built telescopes and navigational tools also constructed colonial bureaucracies and the transatlantic slave trade. Hold both realities simultaneously.

---

## 3. Visual & UI Aesthetic Standards
For any web interface, blog, digital garden, or report:
* **Inspiration:** [nitinpai.in](https://www.nitinpai.in).
* **Palette:**
  * Background: Warm off-white / cream (`#fdfbf7` or `#f7f4ec`).
  * Body Text: Dark charcoal / deep ink (`#2c2a29` or `#1a1918`).
  * Accents: Muted forest green (garden), deep navy/ink blue (blog/reports).
* **Typography:**
  * Headings & Long-Form Prose: High-quality Serif (`Crimson Pro`, `Libre Baskerville`, `Newsreader`).
  * Navigation, Metadata & UI: Clean, legible Sans-Serif (`Inter`, system UI).
* **Simplicity:** High whitespace, generous line height (1.7–1.8), no distracting bells and whistles.

---

## 4. Project Portfolio & Architecture
All core repositories are hosted on GitHub under `@vksgaur`:

1. **Vikas's Blog (`vksgaur/vikas-blog`)**
   * Static engine: Hugo.
   * Posts: Markdown in `content/posts/` with YAML front matter (`title`, `date`, `tags`, `summary`).
   * Deploy: GitHub Actions to GitHub Pages.

2. **Digital Garden (`vksgaur/vikas-garden`)**
   * Static engine: Custom Node.js processor (`build.js`).
   * Notes: Markdown in `notes/` with front matter (`title`, `stage: seedling | growing | evergreen`, `tags`, `summary`).
   * Linking: Double brackets `[[Note Title]]` with automatic bidirectional backlinks.
   * Visualizer: Interactive force-directed canvas graph at `/graph.html`.

3. **Vikas's Reports (`vksgaur/vikas-reports`)**
   * Standalone long-form HTML/CSS deep-dive essays (e.g. Europe's Divergence, Silicon Shield, The Story of Money, China, Japan, Singapore).
   * Features: Sticky table of contents, reading time calculation, reading mode.

4. **Margins / Read-It-Later (`vksgaur/readitlater` / `vksgaur/marginalia`)**
   * Curated reading list, article saver, highlighter, PWA + Chrome Extension.

5. **Hindi Quotes App (`vksgaur/hindi-quotes`)**
   * Curated Hindi & Urdu literature quotes with social media canvas image generator.

---

## 5. Agent Instructions for New Conversations
When starting a conversation or task:
* Check for existing conventions before writing code or content.
* Keep replies concise, structured, and actionable.
* Proactively suggest next steps aligned with the long-term knowledge ecosystem.

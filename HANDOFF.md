# 🧠 Master Project Context & Agent Handoff

> **Purpose:** Keep this file at the root of your projects or copy it to your new system. When starting a conversation on a new computer or under a new account, feed this document to the AI assistant to instantly restore 100% context and continuity.

---

## 1. User & Identity Profile

* **User:** Vikas Gaur
* **Focus Areas:** Deep-dive research, long-form narrative writing, reading and knowledge curation, digital gardens, and web applications.
* **Writing Style & Voice:**
  * In the spirit of Yuval Noah Harari (*Sapiens*) meets Ramachandra Guha and Barbara Tuchman.
  * Serious, narrative journalism written for an intelligent, curious reader.
  * **No academic jargon or hedging.** Abstract concepts must always be grounded in real human stories, specific people, moments, and places.
  * Balanced perspective: Never uncritical celebration of power (e.g. holding both Newton and the slave trade simultaneously).
* **Design Aesthetic & Preferences:**
  * Clean, cream-and-serif aesthetic inspired by [nitinpai.in](https://www.nitinpai.in).
  * Color palette: Off-white/cream background (`#fdfbf7`), rich charcoal body text (`#2c2a29`), deep ink accents.
  * Typography: Serif headers (Crimson Pro, Libre Baskerville), clean sans-serif UI (Inter).
  * Extreme simplicity: Avoid technical friction so Vikas can focus on thinking, reading, and writing.

---

## 2. Active Projects & Repositories

All main projects are hosted on GitHub under user `@vksgaur`:

| Project | What It Is | Tech Stack | GitHub Repo / URL |
| :--- | :--- | :--- | :--- |
| **Vikas's Blog** | Personal long-form blog with cream-and-serif theme | Hugo + GitHub Pages | `vksgaur/vikas-blog`<br>URL: https://vksgaur.github.io/vikas-blog/ |
| **Digital Garden** | Interconnected wiki notes (`[[wiki-links]]`), growth stages (🌱🌿🌳), interactive graph | Custom Node.js builder + GitHub Pages | `vksgaur/vikas-garden`<br>URL: https://vksgaur.github.io/vikas-garden/ |
| **Vikas's Reports** | Deep-dive research reports on history, geopolitics, and money | HTML/CSS standalone reports + GitHub Pages | `vksgaur/vikas-reports`<br>URL: https://vksgaur.github.io/vikas-reports/ |
| **Margins (Read-it-Later)** | Curated reading list, article saver, highlighter, PWA + Chrome Extension | Vanilla JS + Firebase + PWA | `vksgaur/readitlater` / `vksgaur/marginalia` |
| **Hindi Quotes App** | Sahitya quotes from Hindi/Urdu authors with social image generator | Vanilla JS + HTML Canvas | `vksgaur/hindi-quotes` |
| **Curated Articles** | Directory of great long-form articles | Single-page directory | `vksgaur/great-article-website` |

---

## 3. Key Conventions & Workflows

### Digital Garden (`vikas-garden`)
* Notes live as Markdown in `/notes/`.
* Growth stages: `seedling` (🌱), `growing` (🌿), `evergreen` (🌳).
* Links use `[[Note Title]]` wiki-link syntax; backlinks are calculated automatically.
* Visual force graph available at `/graph.html`.
* New notes can be created directly on GitHub.com (`Add file` in `/notes/`), and GitHub Actions auto-deploys in ~45 seconds.

### Vikas's Blog (`vikas-blog`)
* Built with Hugo.
* Posts live in `content/posts/` with YAML front matter (`title`, `date`, `tags`, `summary`).
* Has a one-click `./publish` script that stages, commits, and pushes to trigger GitHub Actions.

### Vikas's Reports (`vikas-reports`)
* Standalone narrative reports (e.g. *The Audacity of Ignorance*, *The Silicon Shield*, *The Story of Money*, *Why Nations Rise and Fall*).
* Reading aids: Sticky table of contents, estimated reading time, dark/zen reading mode.
* Accompanied by a 45-book reading list recommendation guide (*Book_Recommendations.docx*).

---

## 4. How to Resume Work on Any New System / Account

When starting a conversation with any AI agent on a new machine or under a new account, paste this prompt:

```text
I am Vikas Gaur. We are continuing our ongoing development across my projects (Vikas's Blog, Digital Garden, Vikas's Reports, and Margins). 
Please read this HANDOFF document carefully:
1. Adopt my writing style (narrative, engaging, no academic jargon).
2. Maintain my design aesthetic (cream-and-serif, clean, minimal).
3. Be aware of our active GitHub repositories under @vksgaur.
What would you like to work on first?
```

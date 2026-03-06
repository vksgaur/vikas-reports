css_append = """

    /* ── 3. STICKY TABLE OF CONTENTS ── */
    const tocStyle = document.createElement('style');
    tocStyle.textContent = `
    @media (min-width: 1350px) {
      body {
        display: grid !important;
        grid-template-columns: 280px minmax(0, 820px) !important;
        gap: 60px !important;
        justify-content: center !important;
        align-items: start !important;
        max-width: 100% !important;
      }
      body > * {
        grid-column: 2;
      }
      body > nav#TOC {
        grid-column: 1;
        grid-row: 1 / 1000;
        position: sticky;
        top: 60px;
        max-height: calc(100vh - 100px);
        overflow-y: auto;
        background: transparent !important;
        border: none !important;
        border-right: 2px solid var(--vr-accent, #c9a84c) !important;
        padding: 0 24px 0 0 !important;
        margin: 0 !important;
        border-radius: 0 !important;
        scrollbar-width: thin;
        scrollbar-color: rgba(201,168,76,0.3) transparent;
      }
      body > #vr-progress {
        grid-column: 1 / -1;
      }
      nav#TOC h2 {
        margin-top: 0;
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 15pt;
        color: var(--vr-accent, #c9a84c) !important;
      }
      nav#TOC ul {
        padding-left: 0 !important;
        list-style-type: none !important;
      }
      nav#TOC li {
        margin: 12px 0 !important;
        font-size: 10.5pt !important;
        line-height: 1.45 !important;
      }
      nav#TOC a {
        color: inherit !important;
        text-decoration: none !important;
        opacity: 0.65;
        transition: opacity 0.2s, color 0.2s;
        display: block;
      }
      nav#TOC a:hover {
        opacity: 1;
        color: var(--vr-accent, #c9a84c) !important;
      }
    }
    `;
    document.head.appendChild(tocStyle);
"""

with open('enhancements.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we don't append multiple times
if "STICKY TABLE OF CONTENTS" not in content:
    # Append right before the final })();
    pos = content.rfind('})();')
    if pos != -1:
        new_content = content[:pos] + css_append + content[pos:]
        with open('enhancements.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Appended sticky ToC to enhancements.js")
    else:
        print("Could not find end of IIFE")
else:
    print("Already appended")

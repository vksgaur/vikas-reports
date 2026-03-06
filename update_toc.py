import re

with open('enhancements.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# We need to add JS to create the toggle button and the CSS to handle the collapsed state.
# Let's replace the existing ToC block with a new, smarter one.

new_toc_block = """    /* ── 3. COLLAPSIBLE STICKY TABLE OF CONTENTS ── */
    const tocStyle = document.createElement('style');
    tocStyle.textContent = `
    @media (min-width: 1150px) {
      body.has-toc {
        display: grid !important;
        grid-template-columns: 250px minmax(0, 820px) !important;
        gap: 40px !important;
        justify-content: center !important;
        align-items: start !important;
        max-width: 100% !important;
        transition: grid-template-columns 0.3s ease;
      }
      body.has-toc.toc-collapsed {
        grid-template-columns: 0px minmax(0, 820px) !important;
        gap: 0px !important;
      }
      body.has-toc > nav#TOC {
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
        transition: opacity 0.2s ease, transform 0.3s ease;
        opacity: 1;
        transform: translateX(0);
      }
      body.has-toc.toc-collapsed > nav#TOC {
        opacity: 0;
        transform: translateX(-20px);
        pointer-events: none;
      }
      body.has-toc > #vr-progress {
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
      
      /* Toggle Button */
      #toc-toggle-btn {
        position: fixed;
        left: 20px;
        top: 20px;
        z-index: 1000;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: rgba(255,255,255,0.05);
        color: var(--vr-accent, #c9a84c);
        border: 1px solid rgba(201,168,76,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.2s ease;
      }
      :root.light #toc-toggle-btn {
        background: rgba(0,0,0,0.03);
      }
      #toc-toggle-btn:hover {
        background: rgba(201,168,76,0.15);
        transform: scale(1.05);
      }
      body.has-toc #toc-toggle-btn {
        opacity: 1;
        visibility: visible;
      }
      #toc-toggle-btn svg {
        width: 18px;
        height: 18px;
        fill: currentColor;
        transition: transform 0.3s ease;
      }
      body.has-toc.toc-collapsed #toc-toggle-btn svg {
        transform: rotate(180deg);
      }
    }
    `;
    document.head.appendChild(tocStyle);

    // Initialise TOC script
    const tocElement = document.getElementById('TOC');
    if (tocElement) {
        document.body.classList.add('has-toc');
        
        // Check saved preference
        const savedTocState = localStorage.getItem('toc-collapsed');
        if (savedTocState === 'true') {
            document.body.classList.add('toc-collapsed');
        }

        // Create toggle button
        const toggleBtn = document.createElement('button');
        toggleBtn.id = 'toc-toggle-btn';
        toggleBtn.ariaLabel = "Toggle Table of Contents";
        toggleBtn.title = "Toggle Table of Contents";
        toggleBtn.innerHTML = `<svg viewBox="0 0 24 24"><path d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6 1.41-1.41z"/></svg>`;
        document.body.appendChild(toggleBtn);

        toggleBtn.addEventListener('click', () => {
            const isCollapsed = document.body.classList.toggle('toc-collapsed');
            localStorage.setItem('toc-collapsed', isCollapsed);
        });
    }"""

old_toc_block_match = re.search(r'(/\* ── 3\. STICKY TABLE OF CONTENTS ── \*/.*?\n    }\n    `;\n    document\.head\.appendChild\(tocStyle\);)', js_content, re.DOTALL)

if old_toc_block_match:
    js_content = js_content.replace(old_toc_block_match.group(1), new_toc_block)
    with open('enhancements.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Updated ToC block in enhancements.js")
else:
    print("Could not find old ToC block")

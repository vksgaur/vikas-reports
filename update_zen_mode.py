import re

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

zen_css = """
        /* ── ZEN MODE ── */
        body.zen-mode {
            background-color: #fdfcf8 !important;
            color: #2c2925 !important;
            font-family: 'Playfair Display', Georgia, serif !important;
            font-size: 14pt !important;
            line-height: 2 !important;
            max-width: 760px;
        }

        body.zen-mode p {
            font-family: 'Playfair Display', Georgia, serif !important;
        }

        body.zen-mode h1, body.zen-mode h2, body.zen-mode h3 {
            color: #1a1610 !important;
            font-family: 'Playfair Display', Georgia, serif !important;
            text-align: center;
        }

        body.zen-mode #theme-toggle,
        body.zen-mode #toc-toggle-btn,
        body.zen-mode .vr-share-container,
        body.zen-mode #vr-progress,
        body.zen-mode .report-meta-header,
        body.zen-mode header p.author,
        body.zen-mode #vr-related,
        body.zen-mode footer {
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.5s ease;
        }
        
        body.zen-mode header h1 {
            border-bottom: none !important;
            margin-top: 60px;
        }
        
        body.zen-mode .zen-btn {
            opacity: 1 !important;
            pointer-events: auto !important;
            background: rgba(0,0,0,0.03);
            border-color: rgba(0,0,0,0.1);
            color: rgba(0,0,0,0.4);
        }
"""

if '/* ── ZEN MODE ── */' not in css_content:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(zen_css)


with open('enhancements.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

zen_js = """
    /* ── 5. ZEN MODE ── */
    if (currentReport) {
        // Create Zen Button
        const zenBtn = document.createElement('button');
        zenBtn.className = 'vr-share-btn zen-btn';
        zenBtn.title = 'Toggle Zen Mode (Distraction Free Reading)';
        zenBtn.innerHTML = `<svg viewBox="0 0 24 24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 100-16 8 8 0 000 16zM11 7h2v5.586l3.95 3.95-1.414 1.414-4.536-4.536V7z"/></svg>`;
        
        // Find share container to add it there
        const shareCont = document.querySelector('.vr-share-container');
        if (shareCont) {
            shareCont.prepend(zenBtn); // Add to top of share buttons
        } else {
            // Fallback if share container isn't ready
            zenBtn.style.position = 'fixed';
            zenBtn.style.top = '20px';
            zenBtn.style.right = '80px';
            zenBtn.style.zIndex = '1000';
            document.body.appendChild(zenBtn);
        }

        zenBtn.addEventListener('click', () => {
            // If we are showing ToC, collapse it first
            if (document.body.classList.contains('has-toc') && !document.body.classList.contains('toc-collapsed')) {
                document.body.classList.add('toc-collapsed');
            }
            
            document.body.classList.toggle('zen-mode');
            
            // If turning Zen mode off, restore ToC based on localStorage
            if (!document.body.classList.contains('zen-mode')) {
                const savedTocState = localStorage.getItem('toc-collapsed');
                if (savedTocState !== 'true') {
                    document.body.classList.remove('toc-collapsed');
                }
            }
        });
    }
"""

if '/* ── 5. ZEN MODE ── */' not in js_content:
    insert_point = js_content.rfind('})();')
    if insert_point != -1:
        new_content = js_content[:insert_point] + zen_js + js_content[insert_point:]
        with open('enhancements.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Added Zen Mode")


with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = """
        /* ── FILTER BUTTONS ── */
        .filter-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 40px;
        }

        .filter-btn {
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border);
            color: var(--muted);
            padding: 8px 16px;
            border-radius: 100px;
            font-size: 13px;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.25s ease;
        }

        :root.light .filter-btn {
            background: rgba(0,0,0,0.02);
        }

        .filter-btn:hover {
            color: var(--text);
            border-color: rgba(201, 168, 76, 0.4);
            background: rgba(255,255,255,0.06);
            transform: translateY(-2px);
        }

        .filter-btn.active {
            background: var(--gold);
            color: var(--bg);
            border-color: var(--gold);
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(201, 168, 76, 0.3);
        }

        .filter-btn.active:hover {
            transform: none;
        }

        /* ── SCROLL REVEAL ── */
        .reveal-hidden {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), 
                        transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1),
                        border-color 0.25s ease, 
                        box-shadow 0.25s ease;
        }

        .revealed {
            opacity: 1;
            transform: translateY(0);
        }
"""

if '/* ── FILTER BUTTONS ── */' not in content:
    content += new_css
    
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added filter/reveal CSS")

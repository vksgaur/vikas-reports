import re

with open('enhancements.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

dots_js = """
    /* ── 6. CHAPTER PROGRESS DOTS ── */
    if (currentReport) {
        const chapters = document.querySelectorAll('h2');
        if (chapters.length > 2) {
            const dotsStyle = document.createElement('style');
            dotsStyle.textContent = `
            .vr-chapter-dots {
                position: fixed;
                right: 30px;
                top: 50%;
                transform: translateY(-50%);
                display: flex;
                flex-direction: column;
                gap: 10px;
                z-index: 999;
                pointer-events: none;
                transition: opacity 0.5s ease;
            }
            .vr-dot {
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background: rgba(136,136,164,0.3);
                transition: all 0.3s ease;
            }
            .vr-dot.active {
                background: var(--vr-accent, #c9a84c);
                box-shadow: 0 0 8px var(--vr-accent, #c9a84c);
                transform: scale(1.5);
            }
            body.zen-mode .vr-chapter-dots {
                opacity: 0;
            }
            @media (max-width: 1400px) {
                .vr-chapter-dots { display: none; }
            }
            `;
            document.head.appendChild(dotsStyle);

            const dotsContainer = document.createElement('div');
            dotsContainer.className = 'vr-chapter-dots';
            
            chapters.forEach((ch, idx) => {
                const dot = document.createElement('div');
                dot.className = 'vr-dot';
                dot.dataset.idx = idx;
                dotsContainer.appendChild(dot);
            });
            
            document.body.appendChild(dotsContainer);

            const dots = dotsContainer.querySelectorAll('.vr-dot');
            
            window.addEventListener('scroll', () => {
                let currentIdx = -1;
                
                chapters.forEach((ch, idx) => {
                    const rect = ch.getBoundingClientRect();
                    // If the chapter heading is above the middle of the screen
                    if (rect.top < window.innerHeight / 2) {
                        currentIdx = idx;
                    }
                });

                dots.forEach((dot, idx) => {
                    if (idx === currentIdx || (currentIdx === -1 && idx === 0 && window.scrollY < 300)) {
                        dot.classList.add('active');
                    } else {
                        dot.classList.remove('active');
                    }
                });
            }, { passive: true });
        }
    }
"""

if '/* ── 6. CHAPTER PROGRESS DOTS ── */' not in js_content:
    insert_point = js_content.rfind('})();')
    if insert_point != -1:
        new_content = js_content[:insert_point] + dots_js + js_content[insert_point:]
        with open('enhancements.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Added Chapter Progress Dots")


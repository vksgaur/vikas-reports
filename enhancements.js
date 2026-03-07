/* ─────────────────────────────────────────────
   vikas-reports: shared enhancements
   • Reading progress bar
   • "You might also like" section
   ───────────────────────────────────────────── */

(function () {

    /* ── 1. READING PROGRESS BAR ── */
    const barStyle = document.createElement('style');
    barStyle.textContent = `
    #vr-progress {
      position: fixed;
      top: 0; left: 0;
      width: 0%;
      height: 4px;
      background: linear-gradient(90deg, #c9a84c, #e8c96a);
      z-index: 9999;
      transition: width 0.1s linear;
      border-radius: 0 2px 2px 0;
      box-shadow: 0 0 8px rgba(201,168,76,0.6);
    }
    /* dark-mode aware for light pages */
    :root.light #vr-progress {
      background: linear-gradient(90deg, #9a6f0f, #c9a84c);
      box-shadow: 0 0 8px rgba(154,111,15,0.5);
    }

    /* ── YOU MIGHT ALSO LIKE ── */
    #vr-related {
      font-family: 'Inter', 'Segoe UI', sans-serif;
      max-width: 860px;
      margin: 60px auto 0;
      padding: 40px 32px;
      border-top: 2px solid rgba(201,168,76,0.25);
    }
    #vr-related h2 {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 22px;
      font-weight: 700;
      color: #c9a84c;
      margin: 0 0 28px;
      letter-spacing: -0.3px;
    }
    .vr-cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
      gap: 18px;
    }
    .vr-card {
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 22px;
      border: 1px solid rgba(201,168,76,0.18);
      border-radius: 12px;
      text-decoration: none;
      color: inherit;
      background: rgba(255,255,255,0.03);
      transition: transform 0.22s ease, border-color 0.22s ease, background 0.22s ease;
      position: relative;
      overflow: hidden;
    }
    .vr-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--vr-accent, #c9a84c), transparent);
      opacity: 0;
      transition: opacity 0.22s ease;
    }
    .vr-card:hover { transform: translateY(-3px); border-color: rgba(201,168,76,0.45); background: rgba(255,255,255,0.06); }
    .vr-card:hover::before { opacity: 1; }
    .vr-icon { font-size: 28px; line-height: 1; }
    .vr-tag {
      font-size: 9px;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--vr-accent, #c9a84c);
      opacity: 0.85;
    }
    .vr-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 15px;
      font-weight: 700;
      line-height: 1.35;
    }
    .vr-arrow {
      font-size: 13px;
      color: var(--vr-accent, #c9a84c);
      font-weight: 600;
      margin-top: auto;
    }
  `;
    document.head.appendChild(barStyle);

    const bar = document.createElement('div');
    bar.id = 'vr-progress';
    document.body.prepend(bar);

    function updateBar() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
        bar.style.width = pct + '%';
    }
    window.addEventListener('scroll', updateBar, { passive: true });
    updateBar();


        /* ── 3. COLLAPSIBLE STICKY TABLE OF CONTENTS ── */
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
    }

    /* ── 2. YOU MIGHT ALSO LIKE ── */

    const ALL_REPORTS = [
        {
            file: 'The_Original_Blueprint_Japan.html',
            title: 'The Original Blueprint: Japan',
            icon: '🇯🇵',
            tag: 'Japan · Economics · History',
            accent: '#e74c3c',
            related: ['The_Dragon_Awakes_China.html', 'South_Korea_Miracle_Report.html', 'Why_Nations_Rise_and_Fall.html']
        },
        {
            file: 'The_Dragon_Awakes_China.html',
            title: 'The Dragon Awakes: China',
            icon: '🇨🇳',
            tag: 'China · Economics · History',
            accent: '#c0392b',
            related: ['The_Original_Blueprint_Japan.html', 'South_Korea_Miracle_Report.html', 'The_Story_of_Money.html']
        },
        {
            file: 'South_Korea_Miracle_Report.html',
            title: 'The Miracle on the Han River: South Korea',
            icon: '🇰🇷',
            tag: 'Korea · Economics · History',
            accent: '#2980b9',
            related: ['The_Original_Blueprint_Japan.html', 'Singapore_The_Lion_City_Report.html', 'Korean_Cinema_Report.html']
        },
        {
            file: 'The_Silicon_Shield.html',
            title: 'The Silicon Shield: Taiwan',
            icon: '🇹🇼',
            tag: 'Taiwan · Geopolitics · Technology',
            accent: '#27ae60',
            related: ['The_Dragon_Awakes_China.html', 'South_Korea_Miracle_Report.html', 'The_Story_of_Money.html']
        },
        {
            file: 'Singapore_The_Lion_City_Report.html',
            title: 'The Lion City: Singapore',
            icon: '🇸🇬',
            tag: 'Singapore · Economics · Governance',
            accent: '#e74c3c',
            related: ['South_Korea_Miracle_Report.html', 'The_Original_Blueprint_Japan.html', 'Why_Nations_Rise_and_Fall.html']
        },
        {
            file: 'The_Eternal_Future_Brazil.html',
            title: 'The Eternal Future: Brazil',
            icon: '🇧🇷',
            tag: 'Brazil · Economics · History',
            accent: '#27ae60',
            related: ['India_Unfinished_Republic_Report.html', 'Why_Nations_Rise_and_Fall.html', 'The_Story_of_Money.html']
        },
        {
            file: 'India_Unfinished_Republic_Report.html',
            title: 'The Unfinished Republic: India',
            icon: '🇮🇳',
            tag: 'India · Economics · History',
            accent: '#e67e22',
            related: ['The_Eternal_Future_Brazil.html', 'The_Story_of_Money.html', 'Why_Nations_Rise_and_Fall.html']
        },
        {
            file: 'Korean_Cinema_Report.html',
            title: 'Korean Cinema: Hallyu & Beyond',
            icon: '🎬',
            tag: 'Korea · Culture · Cinema',
            accent: '#8e44ad',
            related: ['South_Korea_Miracle_Report.html', 'The_Original_Blueprint_Japan.html', 'Why_Nations_Rise_and_Fall.html']
        },
        {
            file: 'Why_Nations_Rise_and_Fall.html',
            title: 'Why Nations Rise and Fall',
            icon: '🌍',
            tag: 'Global · History · Economics',
            accent: '#16a085',
            related: ['The_Story_of_Money.html', 'India_Unfinished_Republic_Report.html', 'Singapore_The_Lion_City_Report.html']
        },
        {
            file: 'The_Price_That_Rules_the_World.html',
            title: 'The Price That Rules the World: Exchange Rates',
            icon: '💱',
            tag: 'Economics · Global Finance',
            accent: '#4caf82',
            related: ['The_Story_of_Money.html', 'Why_Nations_Rise_and_Fall.html', 'India_Unfinished_Republic_Report.html']
        },
        {
            file: 'The_Story_of_Money.html',
            title: 'The Story of Money: From Cowrie Shells to Crypto',
            icon: '💰',
            tag: 'Economics · History · Philosophy',
            accent: '#8b6914',
            related: ['The_Price_That_Rules_the_World.html', 'India_Unfinished_Republic_Report.html', 'Why_Nations_Rise_and_Fall.html']
        },
        {
            file: 'The_Stock_Market_Story.html',
            title: 'The Stock Market Story: 400 Years of Greed, Genius, and Compounding',
            icon: '📈',
            tag: 'Finance · History · Investing',
            accent: '#1a6b3a',
            related: ['The_Story_of_Money.html', 'India_Unfinished_Republic_Report.html', 'The_Price_That_Rules_the_World.html']
        }
    ];

    // Detect which report we're on by filename
    const currentFile = window.location.pathname.split('/').pop() || '';
    const currentReport = ALL_REPORTS.find(r => r.file === currentFile);
    if (!currentReport) return; // not a report page

    const relatedReports = currentReport.related
        .map(f => ALL_REPORTS.find(r => r.file === f))
        .filter(Boolean);

    if (relatedReports.length === 0) return;

    const section = document.createElement('div');
    section.id = 'vr-related';
    section.innerHTML = `
    <h2>You Might Also Like</h2>
    <div class="vr-cards">
      ${relatedReports.map(r => `
        <a class="vr-card" href="${r.file}" style="--vr-accent:${r.accent}">
          <div class="vr-icon">${r.icon}</div>
          <div class="vr-tag">${r.tag}</div>
          <div class="vr-title">${r.title}</div>
          <div class="vr-arrow">Read → </div>
        </a>
      `).join('')}
    </div>
  `;
    document.body.appendChild(section);



    

    /* ── 4. SOCIAL SHARE BUTTONS ── */
    const shareStyle = document.createElement('style');
    shareStyle.textContent = `
    .vr-share-container {
      position: fixed;
      left: 20px;
      bottom: 40px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      z-index: 1000;
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 0.4s ease, transform 0.4s ease;
      pointer-events: none;
    }
    
    .vr-share-container.visible {
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
    }

    .vr-share-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(201,168,76,0.2);
      color: var(--muted);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      backdrop-filter: blur(4px);
    }
    
    :root.light .vr-share-btn {
      background: rgba(0,0,0,0.03);
      border-color: rgba(154,111,15,0.2);
    }

    .vr-share-btn svg {
      width: 18px;
      height: 18px;
      fill: currentColor;
    }

    .vr-share-btn:hover {
      background: var(--vr-accent, #c9a84c);
      border-color: var(--vr-accent, #c9a84c);
      color: var(--bg) !important;
      transform: scale(1.1);
    }
    
    /* On very small mobile devices, hide it to avoid clutter */
    @media (max-height: 600px) {
       .vr-share-container { display: none !important; }
    }
    `;
    document.head.appendChild(shareStyle);

    // Only add share buttons on report pages
    if (currentReport) {
        const shareContainer = document.createElement('div');
        shareContainer.className = 'vr-share-container';
        
        const urlExp = encodeURIComponent(window.location.href);
        const titleExp = encodeURIComponent(currentReport.title + ' — Research by Vikas Gaur');

        shareContainer.innerHTML = `
          <a class="vr-share-btn" href="https://twitter.com/intent/tweet?url=${urlExp}&text=${titleExp}" target="_blank" rel="noopener noreferrer" title="Share on Twitter/X">
            <svg viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
          </a>
          <a class="vr-share-btn" href="https://wa.me/?text=${titleExp}%20${urlExp}" target="_blank" rel="noopener noreferrer" title="Share on WhatsApp">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 00-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
          </a>
          <button class="vr-share-btn" onclick="navigator.clipboard.writeText(window.location.href); alert('Link copied to clipboard!');" title="Copy Link">
            <svg viewBox="0 0 24 24"><path d="M16 1H4C2.9 1 2 1.9 2 3v14h2V3h12V1zm3 4H8C6.9 5 6 5.9 6 7v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
          </button>
        `;
        document.body.appendChild(shareContainer);

        // Disappear near top of page, fade in when scrolled down
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                shareContainer.classList.add('visible');
            } else {
                shareContainer.classList.remove('visible');
            }
        }, { passive: true });
    }

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
})();

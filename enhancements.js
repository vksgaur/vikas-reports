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


    /* ── 3. STICKY TABLE OF CONTENTS ── */
    const tocStyle = document.createElement('style');
    tocStyle.textContent = `
    @media (min-width: 1150px) {
      body {
        display: grid !important;
        grid-template-columns: 250px minmax(0, 820px) !important;
        gap: 40px !important;
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



    
})();

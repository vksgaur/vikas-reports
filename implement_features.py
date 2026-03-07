with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# CSS for Pull Quotes and Timeline
new_css = """
        /* ── DYNAMIC PULL QUOTES ── */
        .vr-pull-quote {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 24px;
            font-style: italic;
            font-weight: 700;
            line-height: 1.4;
            color: var(--gold);
            text-align: center;
            margin: 60px auto;
            max-width: 90%;
            position: relative;
            padding: 30px 40px;
            background: transparent;
            border: none;
            clear: both;
        }
        
        @media (min-width: 1100px) {
            .vr-pull-quote.float-right {
                float: right;
                width: 340px;
                margin: 10px -80px 20px 40px;
                text-align: right;
                padding: 0;
            }
            .vr-pull-quote.float-left {
                float: left;
                width: 340px;
                margin: 10px 40px 20px -80px;
                text-align: left;
                padding: 0;
            }
        }

        .vr-pull-quote::before {
            content: '“';
            font-family: 'Playfair Display', serif;
            font-size: 80px;
            color: rgba(201, 168, 76, 0.2);
            position: absolute;
            top: -20px;
            left: -10px;
            line-height: 1;
        }
        
        .vr-pull-quote.float-right::before {
            left: -30px;
        }

        :root.light .vr-pull-quote::before {
            color: rgba(154, 111, 15, 0.2);
        }

        /* ── INTERACTIVE TIMELINE SCRUBBER ── */
        .vr-timeline-container {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 80%;
            max-width: 600px;
            height: 4px;
            background: rgba(136,136,164,0.2);
            border-radius: 4px;
            z-index: 990;
            display: flex;
            align-items: center;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.4s ease, visibility 0.4s ease;
            pointer-events: none;
        }

        /* Only show timeline when there are actual dates extracted */
        .vr-timeline-container.active {
            opacity: 1;
            visibility: visible;
        }

        .vr-timeline-progress {
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            background: var(--vr-accent, #c9a84c);
            border-radius: 4px;
            width: 0%;
            transition: width 0.1s linear;
        }

        .vr-timeline-dot {
            position: absolute;
            width: 12px;
            height: 12px;
            background: var(--bg);
            border: 2px solid var(--vr-accent, #c9a84c);
            border-radius: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            transition: left 0.1s linear;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }

        .vr-timeline-label {
            position: absolute;
            top: -25px;
            transform: translateX(-50%);
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            font-weight: 700;
            color: var(--vr-accent, #c9a84c);
            background: var(--surface);
            padding: 2px 8px;
            border-radius: 4px;
            border: 1px solid rgba(201,168,76,0.2);
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        
        .vr-timeline-tick {
            position: absolute;
            width: 2px;
            height: 8px;
            background: rgba(136,136,164,0.4);
            top: 50%;
            transform: translate(-50%, -50%);
        }
        
        .vr-timeline-tick-label {
            position: absolute;
            top: 10px;
            transform: translateX(-50%);
            font-family: 'Inter', sans-serif;
            font-size: 10px;
            color: rgba(136,136,164,0.6);
        }
        
        /* Hide timeline in Zen Mode or on small screens */
        body.zen-mode .vr-timeline-container,
        @media (max-width: 800px) {
            .vr-timeline-container {
                display: none !important;
            }
        }
"""

if '/* ── DYNAMIC PULL QUOTES ── */' not in css_content:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(new_css)

with open('enhancements.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

new_js = """
    /* ── 7. DYNAMIC PULL QUOTES ── */
    if (currentReport) {
        // Find all standard blockquotes
        const blockquotes = document.querySelectorAll('blockquote');
        
        blockquotes.forEach((bq, index) => {
            const text = bq.textContent.trim();
            
            // Only convert short, punchy blockquotes (between 40 and 150 characters) into massive pull quotes
            if (text.length > 40 && text.length < 180) {
                const pullQuote = document.createElement('div');
                pullQuote.className = 'vr-pull-quote';
                
                // Alternate floating left, right, or center
                if (index % 3 === 0) {
                    pullQuote.classList.add('float-right');
                } else if (index % 3 === 1) {
                    pullQuote.classList.add('float-left');
                }
                
                pullQuote.textContent = text;
                
                // Replace the standard blockquote with our premium pull quote
                bq.parentNode.replaceChild(pullQuote, bq);
            }
        });
    }

    /* ── 8. INTERACTIVE TIMELINE SCRUBBER ── */
    if (currentReport) {
        // 1. Extract years from the HTML content
        const paragraphs = document.querySelectorAll('p, h2, h3, li');
        const yearRegex = /\\b(1[0-9]{3}|20[0-2][0-9])\\b/g;
        
        let yearsData = [];
        
        paragraphs.forEach((p, index) => {
            const text = p.textContent;
            let match;
            while ((match = yearRegex.exec(text)) !== null) {
                const year = parseInt(match[0]);
                // Basic sanity check for historical years
                if (year > 1000 && year <= 2026) {
                    yearsData.push({
                        year: year,
                        element: p,
                        top: 0 // Will calculate later
                    });
                }
            }
        });

        if (yearsData.length > 5) {
            // Sort by occurrence in document, not chronologically, because we track scroll progress
            
            // Find min and max chronological years for the scale
            let minYear = 3000;
            let maxYear = 0;
            yearsData.forEach(d => {
                if (d.year < minYear) minYear = d.year;
                if (d.year > maxYear) maxYear = d.year;
            });
            
            // Only build timeline if there is an actual historical span (at least 20 years)
            if (maxYear - minYear > 20) {
                const timelineContainer = document.createElement('div');
                timelineContainer.className = 'vr-timeline-container';
                
                const timelineProgress = document.createElement('div');
                timelineProgress.className = 'vr-timeline-progress';
                timelineContainer.appendChild(timelineProgress);
                
                // Add min/max labels at ends
                timelineContainer.innerHTML += `
                    <div class="vr-timeline-tick" style="left: 0%;"></div>
                    <div class="vr-timeline-tick-label" style="left: 0%;">${minYear}</div>
                    <div class="vr-timeline-tick" style="left: 100%;"></div>
                    <div class="vr-timeline-tick-label" style="left: 100%;">${maxYear}</div>
                `;
                
                const dot = document.createElement('div');
                dot.className = 'vr-timeline-dot';
                dot.style.left = '0%';
                
                const label = document.createElement('div');
                label.className = 'vr-timeline-label';
                label.textContent = minYear;
                dot.appendChild(label);
                
                timelineContainer.appendChild(dot);
                document.body.appendChild(timelineContainer);
                
                // Recalculate physical positions on resize
                const calculatePositions = () => {
                    yearsData.forEach(d => {
                        const rect = d.element.getBoundingClientRect();
                        // Top relative to document
                        d.top = rect.top + window.scrollY; 
                    });
                };
                
                // Wait briefly for images/layout, then calculate
                setTimeout(calculatePositions, 1000);
                window.addEventListener('resize', calculatePositions);
                
                let isTimelineVisible = false;

                window.addEventListener('scroll', () => {
                    // Hide timeline near the very top or bottom of the page
                    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
                    if (window.scrollY < 800 || window.scrollY > maxScroll - 800) {
                        if (isTimelineVisible) {
                            timelineContainer.classList.remove('active');
                            isTimelineVisible = false;
                        }
                        return;
                    } else if (!isTimelineVisible) {
                        timelineContainer.classList.add('active');
                        isTimelineVisible = true;
                    }

                    // Find which year we are currently looking at
                    const currentY = window.scrollY + (window.innerHeight / 2); // Middle of viewport
                    
                    let closestData = yearsData[0];
                    let minDiff = Infinity;
                    
                    yearsData.forEach(d => {
                        const diff = Math.abs(d.top - currentY);
                        if (diff < minDiff) {
                            minDiff = diff;
                            closestData = d;
                        }
                    });
                    
                    if (closestData) {
                        label.textContent = closestData.year;
                        
                        // Calculate percentage along the chronological timeline
                        let pct = ((closestData.year - minYear) / (maxYear - minYear)) * 100;
                        pct = Math.max(0, Math.min(100, pct)); // Clamp
                        
                        dot.style.left = `${pct}%`;
                        timelineProgress.style.width = `${pct}%`;
                    }
                }, { passive: true });
            }
        }
    }
"""

if '/* ── 7. DYNAMIC PULL QUOTES ── */' not in js_content:
    insert_point = js_content.rfind('})();')
    if insert_point != -1:
        new_content = js_content[:insert_point] + new_js + js_content[insert_point:]
        with open('enhancements.js', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Added Pull Quotes and Timeline Scrubber JS")


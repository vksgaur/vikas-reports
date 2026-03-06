import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Filter Tags below the divider, above the grid
filter_html = """
    <div class="filter-container">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="economics">Economics & Finance</button>
        <button class="filter-btn" data-filter="history">History</button>
        <button class="filter-btn" data-filter="asia">Asia</button>
        <button class="filter-btn" data-filter="geopolitics">Geopolitics</button>
    </div>
"""

if 'class="filter-container"' not in content:
    content = content.replace('<div class="section-label">All Reports</div>', 
                             filter_html)

# 2. Add Filter JS
filter_js = """
        // Filter Logic
        const filterBtns = document.querySelectorAll('.filter-btn');
        const cards = document.querySelectorAll('.card');

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.getAttribute('data-filter');

                cards.forEach(card => {
                    const tagText = card.querySelector('.card-tag').textContent.toLowerCase();
                    
                    if (filter === 'all') {
                        card.style.display = 'flex';
                        setTimeout(() => card.style.opacity = '1', 10);
                    } else if (filter === 'economics' && (tagText.includes('economic') || tagText.includes('finance'))) {
                        card.style.display = 'flex';
                        setTimeout(() => card.style.opacity = '1', 10);
                    } else if (filter === 'history' && tagText.includes('history')) {
                        card.style.display = 'flex';
                        setTimeout(() => card.style.opacity = '1', 10);
                    } else if (filter === 'asia' && (tagText.includes('japan') || tagText.includes('china') || tagText.includes('korea') || tagText.includes('taiwan') || tagText.includes('singapore') || tagText.includes('india'))) {
                        card.style.display = 'flex';
                        setTimeout(() => card.style.opacity = '1', 10);
                    } else if (filter === 'geopolitics' && (tagText.includes('geopolitic') || tagText.includes('governance'))) {
                        card.style.display = 'flex';
                        setTimeout(() => card.style.opacity = '1', 10);
                    } else {
                        card.style.opacity = '0';
                        setTimeout(() => card.style.display = 'none', 300);
                    }
                });
            });
        });

        // Scroll Reveal Logic
        const observerOptions = {
            threshold: 0.1,
            rootMargin: "0px 0px -50px 0px"
        };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        cards.forEach(card => {
            card.classList.add('reveal-hidden');
            observer.observe(card);
        });
"""

if '// Filter Logic' not in content:
    content = content.replace('})();\n    </script>', filter_js + '\n        })();\n    </script>')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html with filters and reveal logic")

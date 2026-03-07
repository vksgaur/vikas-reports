import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# 1. Update the Hero Background to the "Map" concept
# We'll use a pure CSS animated topographical pattern
hero_pattern_css = """
        /* ── HERO ── */
        .hero {
            position: relative;
            padding: 120px 24px 100px;
            text-align: center;
            overflow: hidden;
        }

        .hero-bg-map {
            position: absolute;
            inset: -50%;
            width: 200%;
            height: 200%;
            background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23c9a84c' fill-opacity='0.15'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
            opacity: 0.4;
            animation: drift 60s linear infinite;
            pointer-events: none;
            z-index: 0;
        }

        @keyframes drift {
            0% { transform: translateY(0) rotate(0deg); }
            100% { transform: translateY(-10%) rotate(5deg); }
        }

        :root.light .hero-bg-map {
            opacity: 0.15;
            background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%239a6f0f' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        }

        .hero-content {
            position: relative;
            z-index: 10;
        }
        
        .hero::after {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at center, transparent 0%, var(--bg) 80%);
            z-index: 1;
            pointer-events: none;
        }
"""

if '.hero-bg-map' not in css_content:
    # Replace existing .hero block
    css_content = re.sub(r'/\* ── HERO ── \*/.*?\.hero-label \{', hero_pattern_css + "\n        .hero-label {", css_content, flags=re.DOTALL)


# 2. Add Magnetic Hover tracking logic
magnetic_hover_css = """
        /* ── MAGNETIC HOVER CARDS ── */
        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 32px;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            gap: 16px;
            position: relative;
            overflow: hidden;
            transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
        }

        .card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(
                800px circle at var(--mouse-x, -500px) var(--mouse-y, -500px),
                rgba(255, 255, 255, 0.05),
                transparent 40%
            );
            z-index: 0;
            transition: opacity 0.5s;
            opacity: 0;
        }
        
        :root.light .card::before {
            background: radial-gradient(
                800px circle at var(--mouse-x, -500px) var(--mouse-y, -500px),
                rgba(0, 0, 0, 0.03),
                transparent 40%
            );
        }

        .card::after {
            content: '';
            position: absolute;
            inset: -1px;
            background: radial-gradient(
                400px circle at var(--mouse-x, -500px) var(--mouse-y, -500px),
                var(--accent, rgba(201, 168, 76, 0.5)),
                transparent 40%
            );
            z-index: -1;
            opacity: 0;
            transition: opacity 0.5s;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: transparent; /* Hide normal border so after-border shows */
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
        }

        .card:hover::before,
        .card:hover::after {
            opacity: 1;
        }

        .card > * {
            position: relative;
            z-index: 10;
        }
"""

if '800px circle at var(--mouse-x' not in css_content:
    # Replace existing .card styles up to .card-icon
    css_content = re.sub(r'\.card \{.*?\.card-icon \{', magnetic_hover_css + "\n        .card-icon {", css_content, flags=re.DOTALL)


with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# Update HTML structure for Hero
if '<div class="hero-bg-map"></div>' not in content:
    content = content.replace('<section class="hero">', '<section class="hero">\n        <div class="hero-bg-map"></div>\n        <div class="hero-content">')
    content = content.replace('</section>', '</div>\n    </section>')

# Add JS for magnetic hover
magnetic_js = """
        // Magnetic Hover Effect for Cards
        document.getElementById('cards-grid').addEventListener('mousemove', e => {
            for(const card of document.querySelectorAll('.card')) {
                const rect = card.getBoundingClientRect(),
                      x = e.clientX - rect.left,
                      y = e.clientY - rect.top;

                card.style.setProperty("--mouse-x", `${x}px`);
                card.style.setProperty("--mouse-y", `${y}px`);
            }
        });
"""

if 'Magnetic Hover Effect' not in content:
    content = content.replace('<div class="cards">', '<div class="cards" id="cards-grid">')
    content = content.replace('// Scroll Reveal Logic', magnetic_js + '\n        // Scroll Reveal Logic')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Hero map and magnetic cards")

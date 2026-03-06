import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract styles
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    styles = style_match.group(1).strip()
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(styles)
    print("Extracted style.css")
    
    # Replace style block with link
    content = content.replace(style_match.group(0), '<link rel="stylesheet" href="style.css" />')

# Add missing reading times to some cards
replacements = [
    (r'<span>Long-form · Multiple chapters</span>\s*<span class="card-read">Read →</span>',
     r'<span>⏳ 55 min read · Multiple chapters</span>\n                    <span class="card-read">Read →</span>'),
    (r'<span>~18,500 words · 12 chapters</span>', r'<span>⏳ 60 min read · 18k words</span>'),
    (r'<span>~18,000 words · 10 chapters</span>', r'<span>⏳ 60 min read · 18k words</span>'),
    (r'<span>~16,700 words · 11 chapters</span>', r'<span>⏳ 55 min read · 16k words</span>'),
    (r'<span>~16,200 words · 11 chapters</span>', r'<span>⏳ 50 min read · 16k words</span>'),
    (r'<span>~12,600 words · 11 chapters</span>', r'<span>⏳ 45 min read · 12k words</span>'),
    (r'<span>~17,300 words · 12 chapters</span>', r'<span>⏳ 55 min read · 17k words</span>'),
    (r'<span>~17,000 words · 12 chapters</span>', r'<span>⏳ 55 min read · 17k words</span>'),
    (r'<span>~21,000 words · 12 chapters</span>', r'<span>⏳ 70 min read · 21k words</span>'),
    (r'<span>~14,000 words · 13 chapters</span>', r'<span>⏳ 45 min read · 14k words</span>')
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")

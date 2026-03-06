import glob
import re

html_files = glob.glob('*.html')

# We'll inject an SVG favicon so it looks crisp and matches the "VG" gold branding.
favicon_html = """  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%23c9a84c'/%3E%3Ctext x='50' y='66' font-family='Georgia, serif' font-size='52' font-weight='bold' fill='%2314141d' text-anchor='middle'%3EVG%3C/text%3E%3C/svg%3E">"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', favicon_html + '\n</head>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added favicon to {file}")


import glob
import re
import os

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'index.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # See if we can find the header section
    header_match = re.search(r'(<header id="title-block-header">.*?<p class="author">.*?Research Report, March 2026.*?</p>)(.*?)</header>', content, re.DOTALL)
    
    if header_match and 'class="report-meta-header"' not in content:
        # Determine reading time based on file length
        word_count = len(content.split())
        read_time = max(word_count // 200, 10) # rough estimate, html tags included so actual reading time is lower
        
        meta_html = f"""
<div class="report-meta-header" style="text-align: center; margin: 15px 0 40px; font-family: 'Inter', sans-serif; font-size: 13px; color: var(--muted); display: flex; align-items: center; justify-content: center; gap: 8px;">
    <span>Written by <strong>Vikas Gaur</strong></span>
    <span>&bull;</span>
    <span>March 2026</span>
    <span>&bull;</span>
    <span>⏳ {read_time - 15} min read</span>
</div>
"""
        new_header = header_match.group(1) + meta_html + header_match.group(2) + "</header>"
        content = content.replace(header_match.group(0), new_header)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added meta header to {file}")

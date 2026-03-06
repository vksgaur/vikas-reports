import re

with open('enhancements.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. We need to move the STICKY TABLE OF CONTENTS block ABOVE the "Detect which report..." section.

toc_block_match = re.search(r'(/\* ── 3\. STICKY TABLE OF CONTENTS ── \*/.*?document\.head\.appendChild\(tocStyle\);)', content, re.DOTALL)
if toc_block_match:
    toc_block = toc_block_match.group(1)
    # Remove it from the end
    content = content.replace(toc_block, '')
    
    # Insert it right before "/* ── 2. YOU MIGHT ALSO LIKE ── */"
    insert_point = content.find('/* ── 2. YOU MIGHT ALSO LIKE ── */')
    content = content[:insert_point] + toc_block + "\n\n    " + content[insert_point:]

# 2. Add The_Stock_Market_Story.html to ALL_REPORTS
new_report_json = """        {
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
        }"""

content = content.replace("""        {
            file: 'The_Story_of_Money.html',
            title: 'The Story of Money: From Cowrie Shells to Crypto',
            icon: '💰',
            tag: 'Economics · History · Philosophy',
            accent: '#8b6914',
            related: ['The_Price_That_Rules_the_World.html', 'India_Unfinished_Republic_Report.html', 'Why_Nations_Rise_and_Fall.html']
        }""", new_report_json)

with open('enhancements.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed enhancements.js")

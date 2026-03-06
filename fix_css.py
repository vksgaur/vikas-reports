with open('enhancements.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('@media (min-width: 1350px)', '@media (min-width: 1150px)')
text = text.replace('grid-template-columns: 280px minmax(0, 820px) !important;', 'grid-template-columns: 250px minmax(0, 820px) !important;')
text = text.replace('gap: 60px !important;', 'gap: 40px !important;')

# To be safe, let's remove the body > * { grid-column: 2; } and just style the body normally, but grid works well.
# Another possible issue: The user might need a hard refresh if their browser cached the old enhancements.js!

with open('enhancements.js', 'w', encoding='utf-8') as f:
    f.write(text)


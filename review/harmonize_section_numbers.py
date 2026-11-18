from pathlib import Path

root = Path(__file__).resolve().parents[1]
for page in root.glob('*.html'):
    text = page.read_text(encoding='utf-8')
    if 'href="static/services.css"' not in text:
        continue
    if 'href="static/section-numbers.css"' not in text:
        text = text.replace('</head>', '  <link rel="stylesheet" href="static/section-numbers.css">\n</head>', 1)
        page.write_text(text, encoding='utf-8')
        print(page.name)

"""Check local page references, image alternatives and stylesheet braces."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1]
errors = []

class PageCheck(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('src', 'href'):
            value = attrs.get(key, '')
            parsed = urlsplit(value)
            if parsed.path and not parsed.scheme and not parsed.netloc:
                if not (root / unquote(parsed.path)).exists():
                    errors.append(f'{self.page}: missing {value}')
        if tag == 'img' and 'alt' not in attrs:
            errors.append(f'{self.page}: image missing alt')

pages = list(root.glob('*.html'))
for page in pages:
    parser = PageCheck()
    parser.page = page.name
    parser.feed(page.read_text(encoding='utf-8'))
for css in (root/'static').glob('*.css'):
    text = css.read_text(encoding='utf-8')
    if text.count('{') != text.count('}'):
        errors.append(f'{css.name}: unbalanced braces')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: local references and image alternatives across {len(pages)} pages; stylesheet braces.')
assets = sorted((p for p in (root/'static').rglob('*') if p.is_file()), key=lambda p:p.stat().st_size, reverse=True)
print('Static assets total:', round(sum(p.stat().st_size for p in assets)/1048576, 1), 'MB')
for p in assets[:5]:
    print(round(p.stat().st_size/1048576, 1), 'MB', p.relative_to(root))

from pathlib import Path
from PIL import Image
import re,json
r=Path('D:/Winstar website');refs={}
for p in r.glob('*.html'):
    for src in re.findall(r'<img[^>]+src="(static/images/(?:services|slider)/[^"]+)"',p.read_text(encoding='utf-8')):
        if '/cameras/' not in src:refs.setdefault(src,[]).append(p.name)
print(json.dumps(refs,indent=2))

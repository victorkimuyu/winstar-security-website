from pathlib import Path
from html import escape
import re

root = Path(__file__).resolve().parent.parent
names = [re.sub(r'^\d+\.\s*', '', line.strip()) for line in (root/'winstar_clients.txt').read_text(encoding='utf-8').splitlines() if line.strip()]
items = ''.join(f'<li>{escape(name)}</li>' for name in names)
marquee = f'''          <div class="client-marquee-panel">
            <p class="client-marquee-label">Trusted by</p>
            <div class="client-marquee" tabindex="0" aria-label="Winstar clients. Scrolling pauses on hover or keyboard focus.">
              <div class="client-marquee-track">
                <ul class="client-name-list">{items}</ul>
                <ul class="client-name-list" aria-hidden="true">{items}</ul>
              </div>
            </div>
          </div>'''
p = root/'index.html'
t = p.read_text(encoding='utf-8')
pattern = r'(\s*</div>\s*</section>)\s*<!-- Next: Client Logos\. -->'
t, count = re.subn(pattern, lambda _: '\n'+marquee+'\n      </div>\n    </section>', t)
assert count == 1
p.write_text(t,encoding='utf-8')
print(f'Added marquee with {len(names)} client names from supplied file.')

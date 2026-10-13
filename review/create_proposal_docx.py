from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

root = Path(__file__).parent
source = (root / 'website-redesign-proposal-and-quotation.md').read_text(encoding='utf-8-sig')
doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.27), Inches(11.69)
sec.top_margin = sec.bottom_margin = Inches(.65)
sec.left_margin = sec.right_margin = Inches(.7)
sec.header_distance = sec.footer_distance = Inches(.3)
normal = doc.styles['Normal']
normal.font.name = 'Calibri'
normal.font.size = Pt(10.5)
normal.font.color.rgb = RGBColor.from_string('293342')
normal.paragraph_format.space_after = Pt(7)
normal.paragraph_format.line_spacing = 1.08
for name in ['Heading 1', 'Heading 2']:
    s = doc.styles[name]
    s.font.name = 'Calibri'
    s.font.color.rgb = RGBColor.from_string('302D68')
    s.font.size = Pt(13)
    s.paragraph_format.space_before = Pt(12)
    s.paragraph_format.space_after = Pt(6)
    s.paragraph_format.keep_with_next = True
doc.core_properties.title = 'Winstar Security — Website Redesign Proposal & Quotation'
doc.core_properties.subject = 'Website redesign, scope and payment milestones'
doc.core_properties.author = ''
header = sec.header.paragraphs[0]
header.text = 'WINSTAR SECURITY  /  WEBSITE REDESIGN'
header.runs[0].font.size = Pt(8)
header.runs[0].font.color.rgb = RGBColor.from_string('687487')
footer = sec.footer.paragraphs[0]
footer.text = 'PROPOSAL & QUOTATION'
footer.runs[0].font.size = Pt(8)
footer.runs[0].font.color.rgb = RGBColor.from_string('687487')
footer.add_run(' ' * 8 + '•' + ' ' * 8)
field = OxmlElement('w:fldSimple')
field.set(qn('w:instr'), 'PAGE')
footer._p.append(field)

def rich(p, text):
    for i, part in enumerate(re.split(r'\*\*(.*?)\*\*', text)):
        r = p.add_run(part)
        r.bold = bool(i % 2)

def table(lines):
    rows = [[x.strip() for x in line.strip().strip('|').split('|')] for line in lines]
    rows = [r for r in rows if not all(re.fullmatch(r'[-: ]+', c) for c in r)]
    t = doc.add_table(rows=0, cols=len(rows[0]))
    t.autofit = False
    widths = [1.6, 5.27] if len(rows[0]) == 2 else [1.05, 4.52, 1.3]
    for col, w in zip(t.columns, widths): col.width = Inches(w)
    for i, row in enumerate(rows):
        cells = t.add_row().cells
        trpr = t.rows[-1]._tr.get_or_add_trPr()
        trpr.append(OxmlElement('w:cantSplit'))
        if i == 0: trpr.append(OxmlElement('w:tblHeader'))
        for j, (cell, value) in enumerate(zip(cells, row)):
            cell.width = Inches(widths[j])
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(5)
            p.paragraph_format.space_before = Pt(5)
            p.paragraph_format.line_spacing = 1
            rich(p, value)
            for r in p.runs:
                r.font.size = Pt(9.5)
                if i == 0:
                    r.bold = True
                    r.font.color.rgb = RGBColor(255, 255, 255)
            shade = OxmlElement('w:shd')
            shade.set(qn('w:fill'), '302D68' if i == 0 else ('F0F4F8' if i % 2 else 'FFFFFF'))
            cell._tc.get_or_add_tcPr().append(shade)
            if len(cells) == 3 and j == 2: p.alignment = 2
    doc.add_paragraph().paragraph_format.space_after = Pt(0)

lines = source.splitlines()
i = 0
while i < len(lines):
    line = lines[i].strip()
    if not line:
        i += 1
        continue
    if line.startswith('|'):
        block = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            block.append(lines[i]); i += 1
        table(block)
        continue
    if line.startswith('# '):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(line[2:].upper()); r.bold = True; r.font.size = Pt(24)
        r.font.color.rgb = RGBColor.from_string('302D68')
    elif line.startswith('## '):
        p = doc.add_paragraph(line[3:])
        p.paragraph_format.space_after = Pt(12)
        p.runs[0].font.size = Pt(15)
    elif line.startswith('### '):
        title = line[4:]
        if title in ['Sectors and trust signals', 'SEO and Generative Engine Optimization']:
            doc.add_page_break()
        doc.add_heading(title, level=1)
    else:
        p = doc.add_paragraph(style='List Bullet' if line.startswith('- ') else 'Normal')
        rich(p, line[2:] if line.startswith('- ') else line)
    i += 1

out = root / 'Winstar Security - Website Redesign Proposal and Quotation.docx'
doc.save(out)
check = Document(out)
text = '\n'.join(p.text for p in check.paragraphs) + '\n' + '\n'.join(c.text for t in check.tables for r in t.rows for c in r.cells)
for expected in ['Generative Engine Optimization', 'Anti-Corruption Policy', 'KES 65,000', 'KES 25,000', 'KES 20,000']:
    assert expected in text, expected
assert len(check.tables) == 2
assert 'Work begins upon' not in text
print(str(out))
print('Verified: two tables, payment amounts, GEO and policies; no start-work conditions.')

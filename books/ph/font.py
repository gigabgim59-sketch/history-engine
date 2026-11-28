"""완성된 HTML에 실제로 쓰인 글자만 Noto Sans KR에서 잘라 'KRSans'로 심는다.
참고 파일(국제정치사)과 같은 방식: 글꼴 이름 KRSans, 굵기 400 / 500·600 / 700 / 800·900."""
import re, sys, base64, io, os
from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = os.path.join(os.path.dirname(__file__), 'node_modules/@fontsource/noto-sans-kr')
html_path = sys.argv[1]
html = open(html_path, encoding='utf-8').read()
need = {ord(c) for c in html if ord(c) >= 32}
need |= set(range(32, 127)) | {0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2026, 0x00B7, 0x2192, 0x2190, 0x2212}

def ranges(s):
    out = set()
    for part in s.split(','):
        part = part.strip()[2:]
        if '-' in part:
            a, b = part.split('-'); out |= set(range(int(a, 16), int(b, 16) + 1))
        else:
            out.add(int(part, 16))
    return out

def urange(cps):
    cps = sorted(cps); out = []; i = 0
    while i < len(cps):
        j = i
        while j + 1 < len(cps) and cps[j + 1] == cps[j] + 1: j += 1
        out.append(f'U+{cps[i]:x}' + (f'-{cps[j]:x}' if j > i else '')); i = j + 1
    return ','.join(out)

faces = []; total = 0
for src_w, css_w in [('400', '400'), ('600', '500 600'), ('700', '700'), ('800', '800 900')]:
    css = open(f'{ROOT}/{src_w}.css').read()
    for m in re.finditer(r'src: url\(\./files/([^)]+\.woff2)\).*?unicode-range: ([^;]+);', css, re.S):
        fn, ur = m.group(1), m.group(2)
        cps = ranges(ur) & need
        if not cps: continue
        f = TTFont(f'{ROOT}/files/{fn}')
        cps &= set(f.getBestCmap())
        if not cps: continue
        opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = ['*']; opts.name_IDs = ['*']
        sub = subset.Subsetter(opts); sub.populate(unicodes=cps); sub.subset(f)
        buf = io.BytesIO(); f.flavor = 'woff2'; f.save(buf)
        b = base64.b64encode(buf.getvalue()).decode(); total += len(b)
        faces.append(f"@font-face{{font-family:'KRSans';font-style:normal;font-weight:{css_w};font-display:swap;"
                     f"src:url(data:font/woff2;base64,{b}) format('woff2');unicode-range:{urange(cps)}}}")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mathfont import math_face  # 수식이 있으면 Noto Sans Math를 'KRMath'로(DEFECTS E-16)
mf = math_face(html, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'node_modules'))
if mf: faces.append(mf); total += len(mf)
style = '<style>' + ''.join(faces) + '</style>'
html = html.replace('<!--__FONTS__-->', style)
open(html_path, 'w', encoding='utf-8', newline='').write(html)
print('faces', len(faces), 'font KB', total // 1024)

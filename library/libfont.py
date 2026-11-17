"""공통 글꼴: 주어진 글자에 쓰인 문자만 Noto Sans KR에서 잘라 'KRSans' @font-face 묶음을 만든다(engine/font.py와 같은 방식)."""
import re, base64, io, os
from fontTools import subset
from fontTools.ttLib import TTFont
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'node_modules/@fontsource/noto-sans-kr')
def _ranges(s):
    out = set()
    for part in s.split(','):
        part = part.strip()[2:]
        if '-' in part: a, b = part.split('-'); out |= set(range(int(a, 16), int(b, 16) + 1))
        else: out.add(int(part, 16))
    return out
def _urange(cps):
    cps = sorted(cps); out = []; i = 0
    while i < len(cps):
        j = i
        while j + 1 < len(cps) and cps[j + 1] == cps[j] + 1: j += 1
        out.append(f'U+{cps[i]:x}' + (f'-{cps[j]:x}' if j > i else '')); i = j + 1
    return ','.join(out)
def make_faces(text):
    if not os.path.isdir(ROOT): raise SystemExit('library/에서 npm install @fontsource/noto-sans-kr@5 를 먼저 실행할 것')
    need = {ord(c) for c in text if ord(c) >= 32} | set(range(32, 127)) | {0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2026, 0x00B7, 0x2192, 0x2190, 0x2212}
    faces = []
    for src_w, css_w in [('400', '400'), ('600', '500 600'), ('700', '700'), ('800', '800 900')]:
        css = open(f'{ROOT}/{src_w}.css').read()
        for m in re.finditer(r'src: url\(\./files/([^)]+\.woff2)\).*?unicode-range: ([^;]+);', css, re.S):
            fn, ur = m.group(1), m.group(2); cps = _ranges(ur) & need
            if not cps: continue
            f = TTFont(f'{ROOT}/files/{fn}'); cps &= set(f.getBestCmap())
            if not cps: continue
            o = subset.Options(); o.flavor = 'woff2'; o.layout_features = ['*']; o.name_IDs = ['*']
            sb = subset.Subsetter(o); sb.populate(unicodes=cps); sb.subset(f)
            buf = io.BytesIO(); f.flavor = 'woff2'; f.save(buf)
            faces.append(f"@font-face{{font-family:'KRSans';font-style:normal;font-weight:{css_w};font-display:swap;"
                         f"src:url(data:font/woff2;base64,{base64.b64encode(buf.getvalue()).decode()}) format('woff2');unicode-range:{_urange(cps)}}}")
    return ''.join(faces)

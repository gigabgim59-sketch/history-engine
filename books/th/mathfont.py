"""수식 글꼴(DEFECTS E-16): HTML에 MathML(<math>)이 있으면 Noto Sans Math(OpenType MATH 표 포함)를
쓰인 글자만 남겨 'KRMath'로 심는 @font-face 한 줄을 돌려준다. 수식이 없으면 빈 문자열.
화면판(font.py)과 인쇄본(print/render.py)이 함께 쓴다. 글꼴은 restore.sh가 받는 @fontsource/noto-sans-math."""
import base64, io, os, re
from fontTools import subset
from fontTools.ttLib import TTFont

# MathML은 한 글자 <mi>를 수학 이탤릭(U+1D434…)으로 바꿔 그린다. 그 글자들도 남긴다.
ITALIC = set(range(0x1D434, 0x1D49C)) | set(range(0x1D6A4, 0x1D7CC)) | {0x210E, 0x0131, 0x0237}
# 브라우저가 글꼴에서 직접 그리는 기호(근호, 큰 연산자, 늘어나는 괄호의 바탕 글자)도 남긴다. 늘어난 모양은 MATH 표를 따라 함께 남는다
BASIC = set(range(0x20, 0x7F)) | {0x2212, 0x00D7, 0x00B7, 0x2032, 0x2026, 0x22C5, 0x221A, 0x221B, 0x221C, 0x2211, 0x220F, 0x222B, 0x2223, 0x2225, 0x27E8, 0x27E9, 0x2016, 0x23DE, 0x23DF, 0x0302, 0x0303, 0x0304, 0x00AF, 0x2192, 0x2190}


def math_face(html, node_modules):
    blocks = re.findall(r'<math[\s\S]*?</math>', html)
    if not blocks:
        return ''
    src = os.path.join(node_modules, '@fontsource/noto-sans-math/files/noto-sans-math-latin-400-normal.woff2')
    if not os.path.exists(src):
        raise SystemExit('수식 글꼴 없음: ' + src + ' (책 폴더에서 bash restore.sh)')
    text = ''.join(re.sub(r'<[^>]+>', '', b) for b in blocks)
    text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    need = {ord(c) for c in text} | ITALIC | BASIC
    f = TTFont(src)
    need &= set(f.getBestCmap())
    o = subset.Options(); o.flavor = 'woff2'; o.layout_features = ['*']; o.name_IDs = ['*']; o.notdef_outline = True
    s = subset.Subsetter(o); s.populate(unicodes=need); s.subset(f)
    buf = io.BytesIO(); f.flavor = 'woff2'; f.save(buf)
    b = base64.b64encode(buf.getvalue()).decode()
    return ("@font-face{font-family:'KRMath';font-style:normal;font-weight:400;font-display:swap;"
            f"src:url(data:font/woff2;base64,{b}) format('woff2')}}")

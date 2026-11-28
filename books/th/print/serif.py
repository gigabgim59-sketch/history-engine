"""인쇄본 글꼴: Noto Serif CJK KR(CFF)을 책에 쓰인 글자만 남겨 TrueType(glyf)으로 바꾼다.
크로뮴(Skia)은 CFF 글꼴을 PDF에 Type 3로 넣는다(DEFECTS P-02). TrueType으로 바꿔 넣으면 CIDFontType2로 들어간다.
사용: from serif import faces; css = faces(text)  → @font-face 두 개(400, 700), 글꼴 이름 'PSerif'
"""
import base64, io, os
from fontTools.ttLib import TTCollection, TTFont, newTable
from fontTools import subset
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

_FD = os.environ.get('NOTO_SERIF_DIR') or '/usr/share/fonts/opentype/noto'  # 리눅스 밖에서는 글꼴 폴더를 환경 변수로 준다(DEFECTS E-24)
SRC = {400: os.path.join(_FD, 'NotoSerifCJK-Regular.ttc'),
       700: os.path.join(_FD, 'NotoSerifCJK-Bold.ttc')}
EXTRA = ''.join(chr(c) for c in range(0x20, 0x7f)) + '·…‘’“”–—「」『』〈〉《》()[]〔〕%‰°×÷±→←↑↓§'


def _kr(path):
    for f in TTCollection(path).fonts:
        if 'KR' in (f['name'].getDebugName(1) or ''):
            return f
    raise SystemExit(f'KR 글꼴 없음: {path}')


def _to_ttf(font):
    """CFF 윤곽을 2차 곡선으로 바꿔 glyf 표를 만든다(fontTools otf2ttf 방식)."""
    order = font.getGlyphOrder(); gs = font.getGlyphSet(); glyphs = {}
    for name in order:
        pen = TTGlyphPen(gs)
        gs[name].draw(Cu2QuPen(pen, max_err=1.0, reverse_direction=True))
        glyphs[name] = pen.glyph()
    font['loca'] = newTable('loca')
    font['glyf'] = glyf = newTable('glyf')
    glyf.glyphOrder = order; glyf.glyphs = glyphs
    del font['CFF ']
    if 'VORG' in font: del font['VORG']
    glyf.compile(font)
    font['maxp'] = maxp = newTable('maxp')
    maxp.tableVersion = 0x00010000
    for k in ('maxZones', 'maxTwilightPoints', 'maxStorage', 'maxFunctionDefs', 'maxInstructionDefs',
              'maxStackElements', 'maxSizeOfInstructions', 'maxComponentElements'):
        setattr(maxp, k, 0)
    maxp.maxZones = 1; maxp.maxComponentDepth = 0
    maxp.compile(font)
    post = font['post']; post.formatType = 2.0; post.extraNames = []; post.mapping = {}; post.glyphOrder = order
    font['head'].indexToLocFormat = 0; font['head'].glyphDataFormat = 0
    font.sfntVersion = '\0\1\0\0'
    return font


def ttf(weight, text):
    f = _kr(SRC[weight])
    o = subset.Options(); o.layout_features = ['kern', 'liga', 'locl']; o.name_IDs = ['*']; o.notdef_outline = True
    o.hinting = False; o.desubroutinize = True
    s = subset.Subsetter(o); s.populate(text=''.join(sorted(set(text + EXTRA)))); s.subset(f)
    f = _to_ttf(f)
    f['OS/2'].fsType = 0
    b = io.BytesIO(); f.save(b); return b.getvalue()


def faces(text):
    css = ''
    for w in (400, 700):
        data = base64.b64encode(ttf(w, text)).decode()
        css += f"@font-face{{font-family:'PSerif';font-weight:{w};src:url(data:font/ttf;base64,{data}) format('truetype')}}\n"
    return css


if __name__ == '__main__':
    import sys
    t = open(sys.argv[1], encoding='utf-8').read()
    open(sys.argv[2], 'wb').write(ttf(400, t)); print('ok', os.path.getsize(sys.argv[2]))

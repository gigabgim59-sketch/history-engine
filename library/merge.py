"""서가 병합: python3 library/merge.py [출력 경로]
등록부(library/books.json)의 책들을 하나의 서가 HTML로 합친다(기본 출력: library/dist/index.html).

하는 일
1. 책마다 HTML을 읽고, 그 책에 심긴 글꼴(<style>@font-face{font-family:'KRSans'…}</style>)을 떼어 자리표시로 바꾼다.
   글꼴도 자리표시도 없으면 멈춘다(빌드 뒤 font.py를 빠뜨린 경우, DEFECTS E-03).
   서가 안에서 쓰는 연결 스크립트(embed_head.html·embed_tail.html)가 없으면 넣는다.
2. 모든 책과 서가 화면의 글자를 모아 공통 글꼴을 한 번만 만든다.
3. 책을 gzip+base64로 묶어 넣고, 카드·색·권수 문구·PDF 버튼·묶음(grp)을 등록부에서 만든다(DEFECTS L-01).
4. 책 사이 일관성 검사(library/xcheck.py)를 돌려 보고한다. 충돌은 출간 스킬이 처리한다.

등록부의 책 항목: id, t, sub, span, desc, grp, ev, parts, guide, color, colorDark, pdf, html(빌드된 책 HTML 경로),
guideHtml(읽는 법 HTML 경로, 있을 때), source(소스 위치 메모).
"""
import json, re, sys, os, gzip, base64, io, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
# 사용: python3 library/merge.py [--reg 등록부.json] [출력 경로]  — 서재가 여럿이면 등록부를 따로 둔다(기본 library/books.json)
args = sys.argv[1:]
REGP = os.path.join(HERE, 'books.json')
if args[:1] == ['--reg']: REGP = os.path.abspath(args[1]); args = args[2:]
REG = json.load(open(REGP, encoding='utf-8'))
OUT = args[0] if args else os.path.join(HERE, 'dist', 'index.html')
SHELL = open(os.path.join(HERE, 'shell.html'), encoding='utf-8').read()

def kn(n):
    """고유어 수 관형사: 18 → 열여덟, 21 → 스물한. 100 이상은 숫자."""
    one = ['', '한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉']
    ten = ['', '열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    if n <= 0 or n >= 100: return str(n)
    t, o = divmod(n, 10)
    if t == 2 and o == 0: return '스무'
    return ten[t] + one[o]

FONT_RE = re.compile(r"<style>@font-face\{font-family:'KRSans'.*?</style>", re.S)
# 서가 안 iframe에서 쓰는 연결 스크립트: 뒤로 가기 기록을 서가와 맞추고(머리), 읽는 법·본문 사이 이동과 현재 위치를 서가에 알린다(꼬리)
EMB_H = open(os.path.join(HERE, 'embed_head.html'), encoding='utf-8').read()
EMB_T = open(os.path.join(HERE, 'embed_tail.html'), encoding='utf-8').read()
def prep(path, what):
    s = open(path, encoding='utf-8').read()
    if '<!--__LIBFONTS__-->' not in s:
        s, n = FONT_RE.subn('<!--__LIBFONTS__-->', s, count=1)
        if not n: raise SystemExit(f'글꼴 없음: {what} ({path}) — 책 폴더에서 python3 font.py dist/index.html 을 먼저 돌릴 것')
    if EMB_H not in s:
        if s.count('<head>') != 1: raise SystemExit(f'<head>가 하나가 아님: {what}')
        s = s.replace('<head>', '<head>' + EMB_H + '\n', 1)
    if EMB_T not in s:
        if s.count('</body>') != 1: raise SystemExit(f'</body>가 하나가 아님: {what}')
        s = s.replace('</body>', EMB_T + '</body>', 1)
    return s

books = REG['books']
for b in books:
    for k in ('id', 't', 'grp', 'html', 'color', 'colorDark'):
        if not b.get(k): raise SystemExit(f"등록부 항목 {b.get('id')}: '{k}' 없음")
docs = {}
for b in books:
    docs[b['id'] + '.i'] = prep(os.path.join(HERE, '..', b['html']) if not os.path.isabs(b['html']) else b['html'], b['t'])
    if b.get('guide') and b.get('guideHtml'):
        p = b['guideHtml']; docs[b['id'] + '.g'] = prep(p if os.path.isabs(p) else os.path.join(HERE, '..', p), b['t'] + ' 읽는 법')
    elif b.get('guide'):
        raise SystemExit(f"{b['id']}: guide=true인데 guideHtml이 없다")

N = len(books); n = kn(N)
fill = lambda t: t.replace('{n}', n)
grps = []
for b in books:
    if b['grp'] not in grps: grps.append(b['grp'])
def card(b):
    chips = f"<span>{b['parts']}부</span><span>{b['ev']}장</span>" + ('<span>읽는 법 포함</span>' if b.get('guide') else '')
    acts = f'<a class="btn pri" href="#{b["id"]}.i">읽기</a>' + (f'<a class="btn" href="#{b["id"]}.g">읽는 법</a>' if b.get('guide') else '')
    if b.get('pdf'): acts += f'<a class="btn" href="pdf/{H.escape(b["pdf"])}" download title="줄글만 담은 A4 인쇄본">PDF</a>'
    return (f'<article class="card" style="--c:var(--b-{b["id"]})"><div class="span">{H.escape(b["span"])}</div><h3>{H.escape(b["t"])}</h3>'
            f'<p class="s">{H.escape(b["sub"])}</p><p class="d">{H.escape(b["desc"])}</p><div class="chips">{chips}</div><div class="acts">{acts}</div></article>')
shelves = ''.join(f'<h2>{H.escape(g)}<small>{sum(1 for b in books if b["grp"]==g)}권</small></h2><div class="grid">' +
                  ''.join(card(b) for b in books if b['grp'] == g) + '</div>' for g in grps)
order = [i for i in REG.get('order', []) if any(b['id'] == i for b in books)] + [b['id'] for b in books if b['id'] not in REG.get('order', [])]
meta = [{k: b.get(k) for k in ('id', 't', 'sub', 'span', 'desc', 'grp', 'ev', 'parts', 'guide')} for b in books]

# 공통 글꼴: 모든 책·읽는 법·서가 화면에 쓰인 글자
need_txt = ''.join(docs.values()) + SHELL + json.dumps(REG, ensure_ascii=False)
sys.path.insert(0, HERE)
from libfont import make_faces
faces = make_faces(need_txt)

blobs = '\n'.join(f'<script type="application/octet-stream" id="d-{k}">' +
                  base64.b64encode(gzip.compress(v.encode('utf-8'), mtime=0)).decode() + '</script>' for k, v in docs.items())
out = (SHELL
       .replace('<style id="libfonts">__LIBFONTS__</style>', '<style id="libfonts">' + faces + '</style>')
       .replace('__COLORS_LIGHT__', ''.join(f'--b-{b["id"]}:{b["color"]};' for b in books))
       .replace('__COLORS_DARK__', ''.join(f'--b-{b["id"]}:{b["colorDark"]};' for b in books))
       .replace('__STRATA__', ''.join(f'<i style="background:var(--b-{i})"></i>' for i in order))
       .replace('__LIBTITLE__', json.dumps(REG['title'], ensure_ascii=False))
       .replace('__TITLE__', H.escape(REG['title']))
       .replace('__SUB__', H.escape(fill(REG['subTpl'])))
       .replace('__DESC__', H.escape(fill(REG['descTpl']).replace('{titles}', ', '.join(b['t'] for b in books))))
       .replace('__OGDESC__', H.escape(fill(REG['ogdescTpl'])))
       .replace('__LEDE__', fill(REG['lede']))
       .replace('__SHELVES__', shelves)
       .replace('__FOOTER__', H.escape(fill(REG['footerTpl'])))
       .replace('__META__', json.dumps(meta, ensure_ascii=False))
       .replace('__PDF__', json.dumps({b['id']: 'pdf/' + b['pdf'] for b in books if b.get('pdf')}, ensure_ascii=False))
       .replace('__COL__', json.dumps({b['id']: f'var(--b-{b["id"]})' for b in books}, ensure_ascii=False))
       .replace('__BLOBS__', blobs + '\n'))
left = re.findall(r'__[A-Z_]{3,}__', out.replace('<!--__LIBFONTS__-->', ''))
if left: raise SystemExit('채우지 않은 자리: ' + ', '.join(sorted(set(left))))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8', newline='').write(out)
print(f'서가: {N}권({n} 권), 묶음 {len(grps)}, 문서 {len(docs)}, {len(out)//1024//1024}MB → {OUT}')
missing_pdf = [b['id'] for b in books if not b.get('pdf')]
if missing_pdf: print('주의: PDF 버튼이 없는 책', missing_pdf)
# 책 사이 일관성
import subprocess
subprocess.run([sys.executable, os.path.join(HERE, 'xcheck.py')] + [k for k in docs if k.endswith('.i')], cwd=HERE, input=json.dumps({k: v for k, v in docs.items() if k.endswith('.i')}), text=True)

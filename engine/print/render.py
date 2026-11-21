"""A4 인쇄본 만들기: 책 폴더에서 python3 print/render.py [책 HTML, 기본 dist/index.html]
결과: print/<pfx>_a4.pdf. 같은 폴더에 print/book.html(중간본), print/state.json(쪽수·조임)을 남긴다.

하는 일
1. print/make.mjs로 한 문서(앞붙이+본문)를 만든다. 장 표시와 차례는 문서 안 링크다(P-03).
2. 글꼴은 Noto Serif CJK KR을 TrueType으로 바꿔 넣는다. Type 3가 생기지 않는다(P-02).
3. 크로뮴의 북마크로 구획마다 첫 쪽을 찾는다. 숨은 표지(§id§)를 쓰지 않는다(P-01).
4. 마지막 쪽에 몇 줄만 넘어간 구획은 줄 간격을 조여 다시 짠다(P-04, 다섯 단계까지).
5. 차례에 쪽수를 넣어 다시 짜고, 쪽수가 그대로인지 확인한다.
6. 북마크를 '제1부 …', '1. …' 이름으로 다시 달고 제목 정보를 넣는다(P-03).
"""
import json, os, re, subprocess, sys
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from serif import faces
SRC = sys.argv[1] if len(sys.argv) > 1 else 'dist/index.html'
ROOT = os.path.abspath('.')
os.makedirs('print', exist_ok=True)
STP = 'print/state.json'
MAXT = 5
WARNED = False


def make(state):
    json.dump(state, open(STP, 'w'), ensure_ascii=False)
    r = subprocess.run(['node', os.path.join(HERE, 'make.mjs'), SRC], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stdout + r.stderr)
    global WARNED
    if r.stderr.strip() and not WARNED: print(r.stderr.strip()); WARNED = True
    h = open('print/book.html', encoding='utf-8').read()
    text = re.sub(r'<[^>]+>', '', h)
    h = h.replace('/*__FONTS__*/', faces(text), 1)
    open('print/book.html', 'w', encoding='utf-8').write(h)
    return json.load(open('print/seq.json', encoding='utf-8'))


def render(out):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto('file://' + os.path.join(ROOT, 'print/book.html')); pg.wait_for_timeout(400)
        pg.pdf(path=out, prefer_css_page_size=True, print_background=True, outline=True, tagged=True)
        b.close()


def starts(pdf, seq):
    """북마크(문서 순서)에서 구획마다 첫 쪽(1부터)을 읽는다."""
    r = PdfReader(pdf); flat = []
    def walk(items):
        for it in items:
            if isinstance(it, list): walk(it)
            else: flat.append(r.get_destination_page_number(it) + 1)
    walk(r.outline)
    if len(flat) != len(seq):
        sys.exit(f'북마크 {len(flat)}개, 구획 {len(seq)}개: h1·h2를 구획 제목에만 써야 한다')
    return {sid: pgno for (sid, _, _), pgno in zip(seq, flat)}, len(r.pages)


def page_lines(pdf):
    t = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    return [[l for l in pg.splitlines() if l.strip() and not re.fullmatch(r'\s*\d+\s*', l)] for pg in t.split('\f')]


state = json.load(open(STP)) if os.path.exists(STP) else {}
state = {'toc': {}, 'tight': {k: v for k, v in state.get('tight', {}).items()}}
tmp = 'print/_pass.pdf'
# 1~4: 조임 맞추기
for it in range(MAXT + 1):
    S = make(state); seq = S['seq']; render(tmp)
    st, n = starts(tmp, seq); lines = page_lines(tmp)
    order = [x[0] for x in seq]; sparse = []
    for i, sid in enumerate(order):
        lastp = (st[order[i + 1]] - 1) if i + 1 < len(order) else n
        if lastp > st[sid] and len(lines[lastp - 1]) <= 5:
            sparse.append((sid, lastp, len(lines[lastp - 1])))
    grow = [(sid, p, k) for sid, p, k in sparse if state['tight'].get(sid, 0) < MAXT]
    if not grow: break
    for sid, _, _ in grow: state['tight'][sid] = state['tight'].get(sid, 0) + 1
    print(f'조임 {it + 1}회: {len(grow)}구획 ({", ".join(s for s, _, _ in grow[:8])}{"…" if len(grow) > 8 else ""})')
# 5: 차례 쪽수
for it in range(3):
    state['toc'] = {k: v for k, v in st.items()}
    S = make(state); render(tmp)
    st2, n = starts(tmp, seq)
    if st2 == st: break
    st = st2
else:
    sys.exit('차례 쪽수가 맞지 않는다')
# 6: 북마크와 제목 정보
r = PdfReader(tmp); w = PdfWriter(clone_from=r)
if '/Outlines' in w._root_object: del w._root_object['/Outlines']
parent = None
for sid, label, lvl in seq:
    pi = st[sid] - 1
    if lvl == 0: parent = w.add_outline_item(label, pi)
    else: w.add_outline_item(label, pi, parent=parent)
w.add_metadata({'/Title': S['title'], '/Subject': S['sub']})
w.page_mode = '/UseOutlines'
OUT = f"print/{S.get('pfx') or 'book'}_a4.pdf"
w.write(OUT); os.remove(tmp)
left = [(sid, lp, k) for sid, lp, k in sparse] if sparse else []
print(f'-> {OUT}  {n}쪽, 구획 {len(seq)}, 조인 구획 {len(state["tight"])}' + (f', 아직 빈 쪽 {len(left)}' if left else ''))

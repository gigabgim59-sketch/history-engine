"""화면 검사: python3 t1.py <스크린샷 폴더> [책 폴더]
책 폴더(기본: 현재 폴더)의 dist/index.html을 390px·1280px로 열어, 메뉴 화면과 장 몇 개에서
가로 넘침과 스크립트 오류를 찾는다. 결과가 '390 []', '1280 []'이면 통과.
고친 결함(DEFECTS E-02): 경로와 장 id를 손으로 박지 않고 그 책의 자료에서 읽는다."""
import sys, os, json, re
from playwright.sync_api import sync_playwright
O = sys.argv[1]; B = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else '.')
os.makedirs(O, exist_ok=True)
html = os.path.join(B, 'dist', 'index.html')
src = open(html, encoding='utf-8').read()
m = re.search(r'const DATA=(\{.*?\});\n', src, re.S)
D = json.loads(m.group(1)) if m else {'events': [], 'parts': []}
ev = [e['id'] for e in D.get('events', [])]
pick = [ev[i] for i in sorted({0, len(ev)//4, len(ev)//2, (3*len(ev))//4, len(ev)-1}) if ev] if ev else []
hashes = ['#/'] + [f'#/p/{p["id"]}' for p in D.get('parts', [])[:1]] + [f'#/e/{x}' for x in pick]
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (390, 1280):
        pg = b.new_page(viewport={'width': w, 'height': 900}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('file://' + html); pg.wait_for_timeout(500)
        tabs = pg.evaluate("[...document.querySelectorAll('#tabs a[data-v]')].filter(a=>!a.hidden).map(a=>a.getAttribute('href'))")
        for h in hashes + [t for t in tabs if t not in hashes] + ['#/end']:
            pg.evaluate("h=>{location.hash=h}", h); pg.wait_for_timeout(350)
            sw = pg.evaluate("document.documentElement.scrollWidth")
            if sw > w: errs.append(f'{h} overflow {sw}')
            pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
        print(w, errs)
    b.close()

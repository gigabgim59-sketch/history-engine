# 1200x630 미리보기 그림: python3 thumb_make.py → dist/thumbnail.png
import asyncio
from playwright.async_api import async_playwright
OUT = '/home/claude/taiwan/dist/thumbnail.png'
PAPER, INK, MUTED, LINE, ACC = '#f3efe6', '#1f2126', '#6b6e74', '#d6cfc0', '#8a3b22'
PARTS = [('제1부', '바다의 섬', 1624, 1874, '#9a6a1c'), ('제2부', '식민지', 1874, 1945, '#7b3f78'), ('제3부', '중화민국의 대만', 1945, 1987, '#2c7062'), ('제4부', '민주화', 1987, 2026, '#3a5a9c')]
M = [(1624, '1624', '질란디아 성'), (1684, '1684', '청의 편입'), (1895, '1895', '일본 할양'), (1947, '1947', '2·28'), (1987, '1987', '계엄 해제'), (2026, '2026', '오늘')]
X0, X1, Y = 70, 1130, 470
f = lambda y: X0 + (y - 1624) / (2026 - 1624) * (X1 - X0)
svg = []
for no, t, a, b, c in PARTS:
    xa, xb = f(a), f(b)
    svg.append(f'<rect x="{xa}" y="{Y-4}" width="{xb-xa-3}" height="8" fill="{c}"/>')
    svg.append(f'<text x="{xa}" y="{Y-22}" font-family="Noto Serif CJK KR" font-weight="700" font-size="17" fill="{c}">{no}</text>')
for yr, a, b in M:
    x = f(yr); anc = 'end' if yr == 2026 else ('start' if yr == 1624 else 'middle')
    svg.append(f'<line x1="{x}" x2="{x}" y1="{Y-11}" y2="{Y+11}" stroke="{INK}" stroke-width="1.6"/>')
    svg.append(f'<text x="{x}" y="{Y+40}" text-anchor="{anc}" font-family="Noto Serif CJK KR" font-weight="700" font-size="21" fill="{INK}">{a}</text>')
    svg.append(f'<text x="{x}" y="{Y+62}" text-anchor="{anc}" font-size="15" fill="{MUTED}">{b}</text>')
html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;background:{PAPER};color:{INK};font-family:'Noto Sans CJK KR',sans-serif;position:relative}}
.serif{{font-family:'Noto Serif CJK KR',serif}}
.paper{{position:absolute;inset:0;background:radial-gradient(120% 90% at 20% 0%,#f8f5ee 0%,{PAPER} 55%,#ebe5d8 100%)}}
.frame{{position:absolute;inset:22px;border:1px solid {LINE}}}
.seal{{position:absolute;right:70px;top:64px;width:132px;height:132px;border:5px solid #a0372b;border-radius:6px;display:grid;place-items:center;color:#a0372b}}
.seal i{{font-style:normal;font-family:'Noto Serif CJK KR',serif;font-weight:700;font-size:46px;line-height:1.1;writing-mode:vertical-rl;text-align:center}}
</style></head><body><div class="paper"></div><div class="frame"></div>
<div class="seal"><i>臺灣</i></div>
<div style="position:absolute;left:70px;top:62px">
 <div style="font-size:17px;font-weight:700;color:{ACC};letter-spacing:.06em">20개 분기점으로 읽는 대만사</div>
 <div class="serif" style="font-size:80px;font-weight:700;line-height:1.15;margin-top:14px;letter-spacing:-.01em">섬의 주인</div>
 <div style="font-size:27px;color:{MUTED};margin-top:12px;font-weight:500">네덜란드 상관에서 민주 대만까지</div>
 <div style="margin-top:22px;font-size:17px;color:{MUTED};line-height:1.7"><b style="color:{INK}">주권·통치 · 정치 체제 · 경제 · 사회·종족 · 정체성·언어</b><br>다스리는 이가 다섯 번 바뀐 섬, 400년의 이야기</div>
</div>
<svg style="position:absolute;left:0;top:0" width="1200" height="630">{''.join(svg)}</svg>
<div style="position:absolute;left:70px;top:568px;font-size:15px;color:{MUTED}">1624 – 2026 · 4부 20장 · 지도 · 사건 연결망 · 용어</div>
</body></html>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 630})
        await pg.set_content(html); await pg.wait_for_timeout(300); await pg.screenshot(path=OUT); await b.close()
asyncio.run(main())

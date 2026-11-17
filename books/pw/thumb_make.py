# 1200x630 미리보기 그림: python3 thumb_make.py → dist/thumbnail.png
import asyncio
from playwright.async_api import async_playwright
OUT = '/home/claude/postwar/dist/thumbnail.png'
PAPER, INK, MUTED, LINE, ACC = '#f3efe6', '#1f2126', '#6b6e74', '#d6cfc0', '#8a3b22'
PARTS = [('제1부', '', 1945.6, 1952, '#9a6a1c'), ('제2부', '', 1952, 1960, '#7b3f78'), ('제3부', '', 1960, 1973, '#2c7062'), ('제4부', '', 1973, 1985, '#3a5a9c'), ('제5부', '', 1985, 1991, '#a0372b'), ('제6부', '', 1991, 2001, '#5d6b1f'), ('제7부', '', 2001, 2011.3, '#2f6f8f')]
M = [(1945.6, '1945', '패전'), (1964, '1964', '도쿄 올림픽'), (1973, '1973', '석유 위기'), (1989, '1989', '버블의 정점'), (1995, '1995', '지진과 사린'), (2011.3, '2011', '3·11')]
X0, X1, Y = 70, 1130, 470
f = lambda y: X0 + (y - 1945.6) / (2011.3 - 1945.6) * (X1 - X0)
svg = []
for no, t, a, b, c in PARTS:
    xa, xb = f(a), f(b)
    svg.append(f'<rect x="{xa}" y="{Y-4}" width="{xb-xa-3}" height="8" fill="{c}"/>')
    if xb-xa>60: svg.append(f'<text x="{xa}" y="{Y-22}" font-family="Noto Serif CJK KR" font-weight="700" font-size="17" fill="{c}">{no}</text>')
for yr, a, b in M:
    x = f(yr); anc = 'end' if yr == 2011.3 else ('start' if yr == 1945.6 else 'middle')
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
<div class="seal"><i>戦後</i></div>
<div style="position:absolute;left:70px;top:62px">
 <div style="font-size:17px;font-weight:700;color:{ACC};letter-spacing:.06em">70장으로 읽는 전후 일본의 사회·경제·문화</div>
 <div class="serif" style="font-size:64px;font-weight:700;line-height:1.15;margin-top:14px;letter-spacing:-.01em">잃어버린 것과 얻은 것</div>
 <div style="font-size:27px;color:{MUTED};margin-top:12px;font-weight:500">패전에서 3·11까지, 전후 일본 66년</div>
 <div style="margin-top:22px;font-size:17px;color:{MUTED};line-height:1.7"><b style="color:{INK}">사건 · 경제 · 문화 · 시대의 공기</b><br>국가와 기업, 시민과 대중, 세계와 미국 — 세 힘으로 읽는 66년</div>
</div>
<svg style="position:absolute;left:0;top:0" width="1200" height="630">{''.join(svg)}</svg>
<div style="position:absolute;left:70px;top:568px;font-size:15px;color:{MUTED}">1945 – 2011 · 7부 70장 · 경제 지표 · 시대의 공기 · 지도 · 연결망 · 인물 · 요소별 변천</div>
</body></html>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 630})
        await pg.set_content(html); await pg.wait_for_timeout(300); await pg.screenshot(path=OUT); await b.close()
asyncio.run(main())

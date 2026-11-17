# 1200x630 미리보기 그림: python3 thumb_make.py → dist/thumbnail.png
import asyncio
from playwright.async_api import async_playwright
OUT = '/home/claude/japan/dist/thumbnail.png'
PAPER, INK, MUTED, LINE, ACC = '#f3efe6', '#1f2126', '#6b6e74', '#d6cfc0', '#8a3b22'
PARTS = [('제1부', '', 1853, 1877, '#9a6a1c'), ('제2부', '', 1877, 1894, '#7b3f78'), ('제3부', '', 1894, 1912, '#2c7062'), ('제4부', '', 1912, 1927, '#3a5a9c'), ('제5부', '', 1927, 1937, '#a0372b'), ('제6부', '', 1937, 1941.95, '#5d6b1f')]
M = [(1853, '1853', '페리 내항'), (1868, '1868', '메이지 유신'), (1889, '1889', '메이지 헌법'), (1905, '1905', '러일전쟁'), (1925, '1925', '보통선거법'), (1941.95, '1941', '개전 결정')]
X0, X1, Y = 70, 1130, 470
f = lambda y: X0 + (y - 1853) / (1941.95 - 1853) * (X1 - X0)
svg = []
for no, t, a, b, c in PARTS:
    xa, xb = f(a), f(b)
    svg.append(f'<rect x="{xa}" y="{Y-4}" width="{xb-xa-3}" height="8" fill="{c}"/>')
    if xb-xa>60: svg.append(f'<text x="{xa}" y="{Y-22}" font-family="Noto Serif CJK KR" font-weight="700" font-size="17" fill="{c}">{no}</text>')
for yr, a, b in M:
    x = f(yr); anc = 'end' if yr == 1941.95 else ('start' if yr == 1853 else 'middle')
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
<div class="seal"><i>帝国</i></div>
<div style="position:absolute;left:70px;top:62px">
 <div style="font-size:17px;font-weight:700;color:{ACC};letter-spacing:.06em">60개 분기점으로 읽는 근대 일본의 역사</div>
 <div class="serif" style="font-size:80px;font-weight:700;line-height:1.15;margin-top:14px;letter-spacing:-.01em">제국의 길</div>
 <div style="font-size:27px;color:{MUTED};margin-top:12px;font-weight:500">페리 내항에서 진주만 전야까지, 근대 일본 88년</div>
 <div style="margin-top:22px;font-size:17px;color:{MUTED};line-height:1.7"><b style="color:{INK}">천황과 헌정 · 군대와 통수권 · 산업과 재정 · 사회 · 제국</b><br>위로부터, 아래로부터, 바깥으로부터 — 세 힘으로 읽는 88년</div>
</div>
<svg style="position:absolute;left:0;top:0" width="1200" height="630">{''.join(svg)}</svg>
<div style="position:absolute;left:70px;top:568px;font-size:15px;color:{MUTED}">1853 – 1941 · 6부 60장 · 지도 · 무대 연표 · 사건 연결망 · 인물 · 요소별 변천</div>
</body></html>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 630})
        await pg.set_content(html); await pg.wait_for_timeout(300); await pg.screenshot(path=OUT); await b.close()
asyncio.run(main())

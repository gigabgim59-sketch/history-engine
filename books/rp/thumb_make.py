# 1200x630 미리보기 그림: python3 thumb_make.py → dist/thumbnail.png
import asyncio
from playwright.async_api import async_playwright
OUT = '/home/claude/republic/dist/thumbnail.png'
PAPER, INK, MUTED, LINE, ACC = '#f3efe6', '#1f2126', '#6b6e74', '#d6cfc0', '#8a3b22'
PARTS = [('제1부', '', 1640, 1789, '#9a6a1c'), ('제2부', '', 1789, 1799, '#7b3f78'), ('제3부', '', 1799, 1815, '#2c7062'), ('제4부', '', 1815, 1846, '#3a5a9c'), ('제5부', '', 1846, 1852, '#a0372b'), ('제6부', '', 1852, 1875, '#5d6b1f')]
M = [(1640, '1649', '잉글랜드 공화국'), (1762, '1762', '사회계약론'), (1789, '1789', '바스티유'), (1830, '1830', '7월 혁명'), (1848, '1848', '민족의 봄'), (1875, '1875', '제3공화정')]
X0, X1, Y = 70, 1130, 470
f = lambda y: X0 + (y - 1640) / (1875 - 1640) * (X1 - X0)
svg = []
for no, t, a, b, c in PARTS:
    xa, xb = f(a), f(b)
    svg.append(f'<rect x="{xa}" y="{Y-4}" width="{xb-xa-3}" height="8" fill="{c}"/>')
    if xb-xa>60: svg.append(f'<text x="{xa}" y="{Y-22}" font-family="Noto Serif CJK KR" font-weight="700" font-size="17" fill="{c}">{no}</text>')
for yr, a, b in M:
    x = f(yr); anc = 'end' if yr == 1875 else ('start' if yr == 1640 else 'middle')
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
<div class="seal"><i>共和</i></div>
<div style="position:absolute;left:70px;top:62px">
 <div style="font-size:17px;font-weight:700;color:{ACC};letter-spacing:.06em">60개 분기점으로 읽는 유럽 공화주의의 역사</div>
 <div class="serif" style="font-size:80px;font-weight:700;line-height:1.15;margin-top:14px;letter-spacing:-.01em">공화국의 탄생</div>
 <div style="font-size:27px;color:{MUTED};margin-top:12px;font-weight:500">계몽에서 제3공화정까지, 유럽이 왕을 없앤 길</div>
 <div style="margin-top:22px;font-size:17px;color:{MUTED};line-height:1.7"><b style="color:{INK}">주권 · 시민권 · 헌정 구조 · 자유와 권리 · 민족과 교회</b><br>생각 → 결사 → 위기 → 제도 → 전파와 반동, 다섯 고리로 읽는 235년</div>
</div>
<svg style="position:absolute;left:0;top:0" width="1200" height="630">{''.join(svg)}</svg>
<div style="position:absolute;left:70px;top:568px;font-size:15px;color:{MUTED}">1640 – 1875 · 6부 60장 · 지도 · 무대 연표 · 사건 연결망 · 인물 · 요소별 변천</div>
</body></html>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 630})
        await pg.set_content(html); await pg.wait_for_timeout(300); await pg.screenshot(path=OUT); await b.close()
asyncio.run(main())

import json, asyncio, math, sys
from playwright.async_api import async_playwright
D = '/tmp/claude-0/-home-claude/4a153826-8782-5b1f-a4c8-74dc680cb13e/scratchpad/thumb/'
G = json.load(open(D + 'geo.json'))

T1, T2 = '기원과 계승', '그리고 재창조'
SUB = '근동·이란·인도·중앙유라시아·러시아, 6천 년 정체성의 역사'
PAPER, INK, MUTED, LINE, ACC = '#f3efe6', '#1f2126', '#6b6e74', '#d6cfc0', '#8a3b22'
SEG = [('기원', -4000, -500, '#9a6a1c'), ('계승', -500, 1750, '#2c6a5e'), ('재창조', 1750, 2026, '#8a3b22')]
SHARE = [0.30, 0.45, 0.25]

def xmap(x0, x1):
    w = x1 - x0
    def f(y):
        acc = x0
        for (n, a, b, c), s in zip(SEG, SHARE):
            if y <= b or n == '재창조':
                return acc + (min(max(y, a), b) - a) / (b - a) * w * s
            acc += w * s
    return f

CSS = f"""
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;background:{PAPER};color:{INK};font-family:'Noto Sans CJK KR',sans-serif;position:relative}}
.serif{{font-family:'Noto Serif CJK KR',serif}}
.paper{{position:absolute;inset:0;background:radial-gradient(120% 90% at 20% 0%,#f8f5ee 0%,{PAPER} 55%,#ebe5d8 100%)}}
.frame{{position:absolute;inset:22px;border:1px solid {LINE}}}
"""

def title_block(x, y, size=74, sub=24, eyebrow='120개 분기점으로 읽는 정체성사'):
    return f"""<div style="position:absolute;left:{x}px;top:{y}px">
  <div style="font-size:17px;font-weight:700;color:{ACC};letter-spacing:.06em">{eyebrow}</div>
  <div class="serif" style="font-size:{size}px;font-weight:700;line-height:1.16;margin-top:14px;letter-spacing:-.01em">{T1}<br>{T2}</div>
  <div style="font-size:{sub}px;color:{MUTED};margin-top:16px;font-weight:500">{SUB}</div></div>"""

def band(x0, x1, y, labels=True, ms=True):
    f = xmap(x0, x1)
    out = []
    for (n, a, b, c), s in zip(SEG, SHARE):
        xa, xb = f(a), f(b) if n != '재창조' else x1
        out.append(f'<rect x="{xa}" y="{y-3}" width="{xb-xa-3}" height="6" fill="{c}"/>')
        if labels:
            out.append(f'<text x="{xa}" y="{y-20}" font-family="Noto Serif CJK KR" font-weight="700" font-size="26" fill="{c}">{n}</text>')
            span = {'기원': '기원전 4천년기 – 기원전 5세기', '계승': '기원전 4세기 – 18세기', '재창조': '18세기 – 2026'}[n]
            out.append(f'<text x="{xa+ (64 if n!="재창조" else 92)}" y="{y-21}" font-size="14" fill="{MUTED}">{span}</text>')
    if ms:
        M = [(-3000, '기원전 3000', '초원에서 퍼진 말'), (-586, '기원전 586', '바빌론 유수'), (622, '622', '히즈라'),
             (1206, '1206', '칭기즈칸'), (1501, '1501', '시아파 이란'), (1924, '1924', '민족의 경계'), (2026, '2026', '이란 전쟁')]
        for yr, a, b in M:
            x = f(yr)
            anc = 'end' if yr == 2026 else 'middle'
            out.append(f'<line x1="{x}" x2="{x}" y1="{y-9}" y2="{y+9}" stroke="{INK}" stroke-width="1.6"/>')
            out.append(f'<text x="{x}" y="{y+38}" text-anchor="{anc}" font-family="Noto Serif CJK KR" font-weight="700" font-size="21" fill="{INK}">{a}</text>')
            out.append(f'<text x="{x}" y="{y+60}" text-anchor="{anc}" font-size="14" fill="{MUTED}">{b}</text>')
    return ''.join(out)

def mapsvg(x, y, w, opacity=1, dots=True, labels=True):
    W, H = G['W'], G['H']
    k = w / W
    h = H * k
    pc = {'p1': '#9a6a1c', 'p2': '#2c6a5e', 'p3': '#2c6a5e', 'p4': '#2c6a5e', 'p5': '#8a3b22'}
    s = f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{opacity}" width="{w}" height="{h}" viewBox="0 0 {W} {H}">'
    s += f'<path d="{G["land"]}" fill="#e6dfcf" stroke="#c8bda5" stroke-width="1"/>'
    s += f'<path d="{G["borders"]}" fill="none" stroke="#cdc2ab" stroke-width=".7"/>'
    if dots:
        for e in G['ev']:
            s += f'<circle cx="{e["mx"]}" cy="{e["my"]}" r="{5.2 if e["w"]==1 else 3.4}" fill="{pc[e["p"]]}" opacity=".72"/>'
    if labels:
        OFF={'근동·중동':(-38,52),'이란':(18,40),'인도':(0,30),'중앙유라시아':(0,-34),'러시아·동유럽':(0,-30)}
        for r in G['regions']:
            dx,dy=OFF.get(r['n'],(0,0)); r=dict(r,xy=[r['xy'][0]+dx,r['xy'][1]+dy])
            s += f'<text x="{r["xy"][0]}" y="{r["xy"][1]}" text-anchor="middle" font-size="19" font-weight="700" fill="#55585e" letter-spacing="2" stroke="#efe9dc" stroke-width="5" stroke-linejoin="round" paint-order="stroke">{r["n"]}</text>'
    return s + '</svg>'

def footer(x, y, txt='5부 120장 · 용어 391 · 지도·연표·연결망'):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;font-size:15px;color:{MUTED}">{txt}</div>'

# A: 시간 띠
A = f"""<div class="paper"></div><div class="frame"></div>
{title_block(70, 64)}
<div style="position:absolute;right:70px;top:66px;text-align:right;font-size:15px;color:{MUTED};line-height:1.7">근동 · 이란 · 인도<br>중앙유라시아 · 러시아<br><b style="color:{INK}">기원전 4천년기 – 2026</b></div>
<svg style="position:absolute;left:0;top:0" width="1200" height="630">{band(70, 1130, 452)}</svg>
"""

# B: 지도
B = f"""<div class="paper"></div><div class="frame"></div>
{mapsvg(430, 70, 740, opacity=1)}
<div style="position:absolute;left:0;top:0;width:640px;height:630px;background:linear-gradient(90deg,{PAPER} 70%,rgba(243,239,230,0))"></div>
{title_block(70, 92, size=68, sub=21)}
<div style="position:absolute;left:70px;top:404px;width:430px;border-top:1px solid {LINE};padding-top:16px;font-size:16px;color:{MUTED};line-height:1.75">
 <b style="color:{INK}">언어 · 종교 · 정통성 · 이름 · 혈통</b><br>다섯 겹의 정체성이 언제 생겨나고, 누가 잇고,<br>어떻게 다시 지어졌는가
 <div style="margin-top:14px;display:flex;gap:18px;font-size:14px">{''.join(f'<span style="display:inline-flex;align-items:center;gap:6px"><i style="width:9px;height:9px;border-radius:50%;background:{c};display:inline-block"></i>{n}</span>' for n,a,b,c in SEG)}<span>· 점은 사건의 자리</span></div></div>
{footer(70, 566, '기원전 4천년기 – 2026 · 5부 120장')}
"""

# C: 다섯 겹 점 도표
def strata(x0, x1, y0, rh):
    f = xmap(x0, x1)
    axes = [('lang', '언어'), ('rel', '종교'), ('legit', '정통성'), ('name', '이름'), ('blood', '혈통')]
    s = []
    for (n, a, b, c), sh in zip(SEG, SHARE):
        xa, xb = f(a), (f(b) if n != '재창조' else x1)
        s.append(f'<rect x="{xa}" y="{y0-34}" width="{xb-xa-2}" height="{rh*5+40}" fill="{c}" opacity=".06"/>')
        s.append(f'<text x="{xa+8}" y="{y0-12}" font-family="Noto Serif CJK KR" font-weight="700" font-size="20" fill="{c}">{n}</text>')
    for i, (aid, an) in enumerate(axes):
        y = y0 + 12 + i * rh
        s.append(f'<text x="{x0-14}" y="{y+5}" text-anchor="end" font-size="15" font-weight="700" fill="{MUTED}">{an}</text>')
        s.append(f'<line x1="{x0}" x2="{x1}" y1="{y}" y2="{y}" stroke="{LINE}"/>')
        seen = {}
        for ch in sorted([c for c in G['ch'] if c['ax'] == aid], key=lambda c: c['yr']):
            x = f(ch['yr']); col = [c for (n, a, b, c) in SEG if (a <= ch['yr'] <= b) or (n == '재창조' and ch['yr'] > b)][0]
            k = round(x / 7); off = seen.get(k, 0); seen[k] = off + 1
            s.append(f'<circle cx="{x + (off%3)*3.5}" cy="{y + (-4 if off%2 else 0) * (1 if off else 0)}" r="4.6" fill="{col}" opacity=".85"/>')
    return ''.join(s)

C = f"""<div class="paper"></div><div class="frame"></div>
{title_block(70, 60, size=66, sub=21)}
<div style="position:absolute;right:70px;top:66px;text-align:right;font-size:15px;color:{MUTED};line-height:1.7">5부 120장<br><b style="color:{INK}">기원전 4천년기 – 2026</b></div>
<svg style="position:absolute;left:0;top:0" width="1200" height="630">{strata(170, 1130, 380, 36)}</svg>
<div style="position:absolute;left:70px;top:574px;font-size:14px;color:{MUTED}">점 하나는 한 집단의 정체성이 한 사건에서 바뀐 기록 · 모두 {len(G['ch'])}건</div>
"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 630})
        for name, body in (('A', A), ('B', B), ('C', C)):
            html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
            open(D + f'thumb_{name}.html', 'w').write(html)
            await pg.goto('file://' + D + f'thumb_{name}.html'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=D + f'thumb_{name}.png')
        await b.close()
asyncio.run(main())

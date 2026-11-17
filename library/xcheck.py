"""책 사이 일관성 검사: merge.py가 표준 입력으로 {id.i: html} 을 넘긴다. 혼자 쓸 때: python3 library/xcheck.py --from <서가.html>
보고: (1) 같은 저작·이름 붙은 사건이 책마다 다른 연도(3년 이내 차이) (2) 둘 이상의 책에 나오는 '최초' 주장
판단은 사람(출간 스킬)이 한다. 충돌을 고치면 두 책 모두 고친다(LIBRARY §6.6)."""
import sys, json, re, gzip, base64
def data_of(h):
    i = h.find('const DATA=') + 11; d = 0; q = None; esc = False; j = i
    while j < len(h):
        c = h[j]
        if q:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == q: q = None
        elif c in '"\'`': q = c
        elif c == '{': d += 1
        elif c == '}':
            d -= 1
            if d == 0: j += 1; break
        j += 1
    return json.loads(h[i:j])
def flat(v):
    if isinstance(v, str): return v
    if isinstance(v, list): return ''.join(flat(x) for x in v)
    if isinstance(v, dict): return ''.join(flat(x) for x in v.values())
    return ''
if len(sys.argv) > 2 and sys.argv[1] == '--from':
    s = open(sys.argv[2], encoding='utf-8').read()
    docs = {m.group(1): gzip.decompress(base64.b64decode(m.group(2).strip())).decode() for m in re.finditer(r'<script type="application/octet-stream" id="d-([a-z]{2}\.i)">(.*?)</script>', s, re.S)}
else:
    docs = json.loads(sys.stdin.read())
KIND = '헌법|조약|선언|협정|회의|칙령|강화|협약|공의회|헌장'
pairs = {}; first = {}
for k, h in docs.items():
    bid = k.split('.')[0]
    try: D = data_of(h)
    except Exception as e: print('자료를 읽지 못함', k, e); continue
    for e in D.get('events', []):
        t = flat(D.get('body', {}).get(e['id'], {})) + ' ' + (e.get('s') or '')
        for m in re.finditer(r'(\d{3,4})년[^.。]{0,25}?([『「][^』」]{2,30}[』」])', t): pairs.setdefault(m.group(2), []).append((int(m.group(1)), bid))
        for m in re.finditer(r'(\d{3,4})년(?:의)? ((?:[가-힣]{2,8} )?[가-힣]{2,8} ?(?:' + KIND + r'))(?![가-힣])', t): pairs.setdefault(re.sub(r'\s+', ' ', m.group(2)), []).append((int(m.group(1)), bid))
        for m in re.finditer(r'([가-힣]{2,10}) 최초의 ([가-힣 ]{2,16}?)(?:이|가|을|를|은|는|으로|로|였|이었|의|에)', t):
            first.setdefault((m.group(1) + ' 최초의 ' + m.group(2)).strip(), []).append(bid)
rep = []
for key, l in pairs.items():
    books = {b for _, b in l}
    if len(books) < 2: continue
    ys = sorted({y for y, _ in l})
    if len(ys) < 2 or ys[-1] - ys[0] > 3: continue
    rep.append(f'{key}: ' + ' / '.join(f"{y}({','.join(sorted({b for yy, b in l if yy == y}))})" for y in ys))
fr = [f'{k}: {", ".join(sorted(set(v)))}' for k, v in first.items() if len(set(v)) >= 2]
print(f'책 사이 연도 엇갈림 {len(rep)}건' + (':\n' + '\n'.join(rep) if rep else ''))
print(f"둘 이상의 책에 나오는 '최초' 주장 {len(fr)}건" + (':\n' + '\n'.join(fr) if fr else ''))

"""기존 서가 HTML에서 책 문서를 꺼낸다: python3 library/extract.py <서가.html>
library/build/<id>.html, <id>.guide.html 로 저장하고(글꼴 자리표시 상태 그대로), 등록부의 html·guideHtml 경로를 채운다.
소스가 없는 책을 다시 병합하거나 정비할 때 쓴다. build/는 저장소에 올리지 않는다(.gitignore)."""
import sys, re, gzip, base64, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
s = open(sys.argv[1], encoding='utf-8').read()
os.makedirs(os.path.join(HERE, 'build'), exist_ok=True)
got = {}
for m in re.finditer(r'<script type="application/octet-stream" id="d-([a-z]{2})\.([ig])">(.*?)</script>', s, re.S):
    i, v, b = m.groups(); h = gzip.decompress(base64.b64decode(b.strip())).decode('utf-8')
    fn = f'build/{i}.html' if v == 'i' else f'build/{i}.guide.html'
    open(os.path.join(HERE, fn), 'w', encoding='utf-8').write(h); got.setdefault(i, {})[v] = 'library/' + fn
reg = json.load(open(os.path.join(HERE, 'books.json'), encoding='utf-8'))
for b in reg['books']:
    if b['id'] in got:
        b.setdefault('html', got[b['id']]['i'])
        if 'g' in got[b['id']]: b.setdefault('guideHtml', got[b['id']]['g'])
json.dump(reg, open(os.path.join(HERE, 'books.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('꺼낸 책', len(got), sorted(got))

"""인쇄본 검사: python3 checks/pdfcheck.py <책>_a4.pdf
실패 조건: 숨은 표지(§…§) > 0, Type 3 글꼴, 북마크 없음, 제목 정보 없음. 보고: 거의 빈 쪽."""
import sys, subprocess, re
from pypdf import PdfReader
f = sys.argv[1]; bad = []; note = []
txt = subprocess.run(['pdftotext', '-layout', f, '-'], capture_output=True, text=True).stdout
mk = re.findall(r'§[A-Za-z0-9_]+§', txt)
if mk: bad.append(f'숨은 표지 {len(mk)}개')
fonts = subprocess.run(['pdffonts', f], capture_output=True, text=True).stdout
t3 = [l.split()[0] for l in fonts.splitlines()[2:] if 'Type 3' in l]
if t3: bad.append(f'Type 3 글꼴 {len(t3)}개 ({", ".join(sorted(set(t3))[:3])})')
r = PdfReader(f)
if not r.outline: bad.append('북마크 없음')
if not (r.metadata and r.metadata.get('/Title')): bad.append('제목 정보 없음')
for i, p in enumerate(txt.split('\f')):
    lines = [l for l in p.splitlines() if l.strip()]
    if 0 < len(lines) <= 3 and i > 3: note.append(f'{i+1}쪽(PDF) 거의 빈 쪽: {len(lines)}줄')
print(f'{len(r.pages)}쪽'); print('실패: ' + '; '.join(bad) if bad else '형식 통과')
if note: print('확인할 것:\n' + '\n'.join(note[:20]))
sys.exit(1 if bad else 0)

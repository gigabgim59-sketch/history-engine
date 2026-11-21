"""『계몽의 갈래』 정오 7 (2026-11-21): 묶음 1 독립 검수 out_whole 가운데 고친 것.
(검수 번호, 옛 문구, 새 문구). 옛 문구는 소스 전체에서 꼭 한 번 나와야 한다."""
import glob, sys, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
E = [
('W-1', '1682년 로테르담에 망명한 위그노 피에르 벨은', '1681년 로테르담으로 옮긴 위그노 피에르 벨은 1682년'),
('W-1', '1680년 겨울, 유럽의 하늘에 거대한 혜성이 나타났고, 로테르담의 망명 철학자 ', '1680년 겨울, 유럽의 하늘에 거대한 혜성이 나타났고, 이듬해 로테르담으로 옮긴 철학자 '),
('W-5', '아도르노와 하이에크의 비판은 모두 이 줄기의 상속자였다[[l66]][[l67]].', '아도르노와 하이에크의 비판은 모두 이 줄기의 상속자였다[[l66]][[l67]][[l70]].'),
('W-11', '파리의 루이 16세는 개신교도에게 시민의 지위를 주며', '파리의 루이 16세는 개신교도의 결혼과 출생, 사망을 법으로 인정하며'),
('W-11', '프랑스의 개신교도에게 시민의 지위를 준 칙령.', '프랑스 개신교도의 결혼과 출생, 사망을 법으로 인정한 칙령.'),
('W-12', '토크빌은 의회 편에, 마르크스는 노동자 편에 섰다.', '토크빌은 의회 편에 섰고, 쾰른에서 『신라인 신문』을 내던 마르크스는 노동자 편에서 썼다.'),
('W-19', '그 관념들은 1776년과 1787년 아메리카의 헌법이 되었다[[l35]].', '그 관념들은 1776년의 독립 선언과 1787년의 헌법이 되었다[[l35]].'),
('W-25', "a:'Lewis Namier',o:'1944'", "a:'Lewis Namier',o:'1946(강연 1944)'"),
]
files = [f for f in glob.glob('*.mjs') if not f.startswith('people') and f not in ('build.mjs', 'geo.mjs', 'addp.mjs', 'atcheck.mjs', 'chk.mjs', 'ppcheck.mjs')]
src = {f: open(f, encoding='utf-8').read() for f in files}
bad = 0
for no, old, new in E:
    hits = [f for f in files if old in src[f]]; cnt = sum(src[f].count(old) for f in files)
    if cnt != 1: print(f'!! {no}: {cnt}곳 {hits} :: {old[:50]}'); bad += 1; continue
    src[hits[0]] = src[hits[0]].replace(old, new)
if bad: sys.exit(f'{bad}건 실패, 아무것도 쓰지 않음')
for f in files: open(f, 'w', encoding='utf-8').write(src[f])
print(f'{len(E)}건 적용')

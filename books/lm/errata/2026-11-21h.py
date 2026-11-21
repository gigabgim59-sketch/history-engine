"""『계몽의 갈래』 정오 8 (2026-11-21): 묶음 1 독립 검수 out_whole 가운데 고친 것(둘째 묶음).
(검수 번호, 옛 문구, 새 문구). 옛 문구는 소스 전체에서 꼭 한 번 나와야 한다."""
import glob, sys, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
E = [
('W-9', "'1914년 이후 계몽의 세 갈래는", "'19세기 말 이후 계몽의 세 갈래는"),
('W-10', "'이 부가 끝나는 1730년 무렵,", "'첫째, 이 부가 끝나는 1730년 무렵,"),
('W-10', "'이 부가 끝나는 1760년 무렵,", "'첫째, 이 부가 끝나는 1760년 무렵,"),
('W-10', "'이 부가 끝나는 1789년,", "'첫째, 이 부가 끝나는 1789년,"),
('W-10', "'이 부가 끝나는 1830년,", "'첫째, 이 부가 끝나는 1830년,"),
('W-10', "'이 부가 끝나는 1890년 무렵,", "'첫째, 이 부가 끝나는 1890년 무렵,"),
('W-16', '왕립학회를 세웠고, 그 표어는 ‘누구의 말도 믿지 말라’였다.', '왕립학회를 세웠고, 1663년 무렵부터 ‘누구의 말도 믿지 말라’를 표어로 삼았다.'),
('W-17', '1838년 ‘사회학’이라는 말을 만들었다.', '1838년 ‘사회학’이라는 말을 지어 널리 퍼뜨렸다.'),
('W-18', '노예가 스스로 자유를 쟁취한 첫 혁명이었다.', '노예 봉기가 독립 국가를 세운 첫 사례였다.'),
('W-20', '파시즘은 계몽 자체를 적으로 삼았다.', '파시즘은 스스로를 1789년의 원칙과 계몽에 맞선 운동이라 했다.'),
('W-26', '수십만 명이 망명했다.', '15만~20만 명(추정)이 망명했다.'),
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

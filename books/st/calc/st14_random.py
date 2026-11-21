"""st14: 한 줄로 놓인 밭 16구획, 비옥도가 오른쪽으로 갈수록 높아진다(선형 경향 + 잡음). 처리 효과는 0(귀무가설 참).
(가) 균형 배치 ABBAABBAABBAABBA, (나) 무작위 배치. 처리 차 추정치의 퍼짐과, 보통의 t 검정(5%)이 기각하는 비율.
그리고 피셔의 무작위화 검정: 작은 실험(4+4)에서 관측 차의 순열 p값."""
import numpy as np, itertools
from scipy import stats
rng = np.random.default_rng(14); N = 16; R = 20000; trend = np.linspace(0, 3, N)
bal = np.array(list('ABBAABBAABBAABBA')) == 'A'
eb, er, rb, rr = [], [], 0, 0
for _ in range(R):
    y = trend + rng.normal(0, 1, N)
    a = bal; d = y[a].mean() - y[~a].mean(); eb.append(d); rb += stats.ttest_ind(y[a], y[~a]).pvalue < .05
    a = np.zeros(N, bool); a[rng.choice(N, 8, replace=False)] = True; d = y[a].mean() - y[~a].mean(); er.append(d); rr += stats.ttest_ind(y[a], y[~a]).pvalue < .05
print(f'균형: 차의 표준편차 {np.std(eb):.3f}, t검정 기각률 {rb/R:.3f}')
print(f'무작위: 차의 표준편차 {np.std(er):.3f}, t검정 기각률 {rr/R:.3f}')
y = np.array([5.1, 6.3, 5.8, 6.9, 4.7, 5.0, 5.5, 4.9]); tr = np.array([1, 1, 1, 1, 0, 0, 0, 0], bool)
obs = y[tr].mean() - y[~tr].mean(); cnt = tot = 0
for c in itertools.combinations(range(8), 4):
    m = np.zeros(8, bool); m[list(c)] = True; tot += 1; cnt += (y[m].mean() - y[~m].mean()) >= obs - 1e-12
print(f'무작위화 검정: 관측 차 {obs:.3f}, 70가지 배치 중 {cnt}가지가 그 이상 → 한쪽 p={cnt/tot:.4f}')

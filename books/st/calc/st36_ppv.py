"""st36: (1) 이오아니디스(2005)의 식(편향 없음): 유의한 발견이 참일 확률 PPV = (1-β)R / ((1-β)R + α), R=참 관계 대 없는 관계의 사전 승산.
(2) 시먼스 외(2011) 식의 유연성 모의: 귀무가설 참, 집단당 20명. 종속 변수 둘(상관 0.5)과 그 평균, 유의하지 않으면 10명씩 더 모으기. 하나라도 p<0.05면 '발견'."""
import numpy as np
from scipy import stats
for R in [1, 0.25, 0.1]:
    print(f'R={R}:', ' '.join(f'검정력 {pw}: {pw*R/(pw*R+.05):.2f}' for pw in [0.8, 0.5, 0.2]))
rng = np.random.default_rng(36); N = 20000; fp = 0; fp1 = 0
cov = [[1, .5], [.5, 1]]
def anyp(a, b):
    ps = [stats.ttest_ind(a[:, j], b[:, j]).pvalue for j in (0, 1)] + [stats.ttest_ind(a.mean(1), b.mean(1)).pvalue]
    return min(ps) < .05, ps[0] < .05
for _ in range(N):
    a = rng.multivariate_normal([0, 0], cov, 30); b = rng.multivariate_normal([0, 0], cov, 30)
    hit, single = anyp(a[:20], b[:20]); fp1 += single
    if not hit: hit, _ = anyp(a, b)
    fp += hit
print(f'정해 둔 한 번의 검정 {fp1/N:.3f}, 두 변수·평균·추가 모집을 섞으면 {fp/N:.3f}')

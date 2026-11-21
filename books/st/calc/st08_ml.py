"""st08: (1) 코시 분포의 위치: 표본 평균, 중앙값, 최대가능도의 퍼짐(피셔가 모멘트법을 비판한 맥락의 예).
(2) 네이만·스콧(1948): 쌍마다 평균이 다르고 분산이 같은 자료에서 분산의 최대가능도 추정량은 σ²/2로 간다."""
import numpy as np
from scipy import optimize
rng = np.random.default_rng(5); R = 4000; n = 25
mean, med, mle = [], [], []
for _ in range(R):
    x = rng.standard_cauchy(n)
    mean.append(x.mean()); med.append(np.median(x))
    nll = lambda t: np.sum(np.log1p((x - t) ** 2))
    mle.append(optimize.minimize_scalar(nll, bracket=(np.median(x) - 1, np.median(x) + 1)).x)
q = lambda a: np.subtract(*np.percentile(a, [75, 25]))
print(f'코시 n={n}: 사분위 범위  평균 {q(mean):.2f}  중앙값 {q(med):.3f}  최대가능도 {q(mle):.3f}')
for pairs in [10, 100, 1000, 10000]:
    mu = rng.normal(0, 5, pairs); x = mu[:, None] + rng.normal(0, 1, (pairs, 2))
    s2 = np.mean((x - x.mean(1, keepdims=True)) ** 2)
    print(f'쌍 {pairs:>5}: 최대가능도 σ² 추정 {s2:.3f} (참값 1, 극한 0.5), 보정(×2) {2*s2:.3f}')

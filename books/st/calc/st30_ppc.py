"""st30: 사후 예측 점검. 가상 자료: 음이항으로 만든 과대 산포 계수 자료 50개(평균 4, 분산 약 12). 모형: 포아송, 사전 Gamma(0.001,0.001).
검정량 T=분산/평균. 사후 예측 p값 = P(T(반복) ≥ T(관측) | 자료)."""
import numpy as np
rng = np.random.default_rng(30)
y = rng.negative_binomial(2, 2/6, 50)  # 평균 4, 분산 12
T = lambda v: v.var(ddof=1) / v.mean()
a, b = 0.001 + y.sum(), 0.001 + len(y)
lam = rng.gamma(a, 1/b, 5000)
rep = np.array([T(rng.poisson(l, len(y))) for l in lam])
print(f'관측 평균 {y.mean():.2f}, 분산 {y.var(ddof=1):.2f}, T={T(y):.2f}; 반복 T의 95% 범위 {np.percentile(rep,2.5):.2f}–{np.percentile(rep,97.5):.2f}; 사후 예측 p={np.mean(rep>=T(y)):.4f}')

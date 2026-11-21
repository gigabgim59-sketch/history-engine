"""st11: (1) 정규 평균 95% 신뢰구간의 장기 포함률. (2) 이번 구간에 대한 말: X1,X2 ~ U(θ-1/2, θ+1/2), 구간 [min,max]의 포함률은 50%.
그러나 두 값의 간격이 1/2 이상이면 구간은 θ를 반드시 포함하고, 간격이 작으면 포함 확률이 낮다(조건부 포함률)."""
import numpy as np
rng = np.random.default_rng(11); R = 400000
x = rng.normal(0, 1, (20000, 10)); m = x.mean(1); h = 1.96 / 10 ** 0.5
print('정규 95% 구간 포함률', round(np.mean(np.abs(m) < h), 4))
u = rng.uniform(-.5, .5, (R, 2)); lo, hi = u.min(1), u.max(1); cov = (lo < 0) & (hi > 0); d = hi - lo
print('균등 두 점 [min,max] 전체 포함률', round(cov.mean(), 4))
for a, b in [(0, .1), (.1, .25), (.25, .5), (.5, 1)]:
    s = (d >= a) & (d < b); print(f'  간격 {a}–{b}: 비율 {s.mean():.3f}, 포함률 {cov[s].mean():.3f}')

"""st29: (1) 메트로폴리스 표본으로 켤레가 아닌 사후를 셈하고 격자 적분과 견준다. 자료: 코시 위치 모형 x=(-1.2, 0.3, 0.8, 1.5, 9.0)(설명용), 사전 N(0, 10²).
(2) 부트스트랩: 치우친 표본 30개(지수분포, 고정 난수)의 중앙값의 표준오차와 95% 백분위 구간."""
import numpy as np
x = np.array([-1.2, 0.3, 0.8, 1.5, 9.0])
logp = lambda t: -np.sum(np.log1p((x - t)**2)) - t**2 / 200
g = np.linspace(-20, 30, 200001); lp = np.array([logp(t) for t in g[::10]]); gg = g[::10]
w = np.exp(lp - lp.max()); w /= w.sum(); mean_grid = np.sum(w * gg)
rng = np.random.default_rng(29); t = 0.0; cur = logp(t); draws = []
for i in range(60000):
    prop = t + rng.normal(0, 1.5); new = logp(prop)
    if np.log(rng.uniform()) < new - cur: t, cur = prop, new
    if i >= 10000: draws.append(t)
draws = np.array(draws)
print(f'사후 평균: 격자 적분 {mean_grid:.3f}, 메트로폴리스 {draws.mean():.3f}; 95% 구간(메트로폴리스) {np.percentile(draws,2.5):.2f}–{np.percentile(draws,97.5):.2f}')
s = np.random.default_rng(7).exponential(1.0, 30)
B = np.array([np.median(np.random.default_rng(100+b).choice(s, 30)) for b in range(4000)])
print(f'표본 중앙값 {np.median(s):.3f}, 부트스트랩 표준오차 {B.std(ddof=1):.3f}, 95% 백분위 구간 {np.percentile(B,2.5):.3f}–{np.percentile(B,97.5):.3f}')

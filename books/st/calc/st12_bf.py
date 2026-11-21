"""st12: 베렌스–피셔 문제. 두 정규 표본, 분산이 다르고 모른다. 평균 차의 95% 구간을
(가) 베렌스–피셔 기준 구간(기준 분포 δ=d−(s1/√n1)T1+(s2/√n2)T2의 모의), (나) 웰치 근사 t 구간으로 셈하고
반복 표집의 포함률을 견준다. n1=5, n2=20, σ1/σ2를 바꾼다."""
import numpy as np
from scipy import stats
rng = np.random.default_rng(12); n1, n2 = 5, 20; R = 6000; M = 4000
T1 = stats.t(n1-1).rvs((M,), random_state=rng); T2 = stats.t(n2-1).rvs((M,), random_state=rng)
for r in [0.2, 1, 5]:
    cb = cw = 0
    for _ in range(R):
        a = rng.normal(0, r, n1); b = rng.normal(0, 1, n2)
        d = a.mean() - b.mean(); s1, s2 = a.std(ddof=1)/n1**.5, b.std(ddof=1)/n2**.5
        f = d - s1*T1 + s2*T2; lo, hi = np.percentile(f, [2.5, 97.5]); cb += lo < 0 < hi
        v = (s1**2+s2**2)**2/(s1**4/(n1-1)+s2**4/(n2-1)); h = stats.t(v).ppf(.975)*(s1**2+s2**2)**.5; cw += abs(d) < h
    print(f'σ1/σ2={r}: 포함률 기준 구간 {cb/R:.3f}  웰치 {cw/R:.3f}')

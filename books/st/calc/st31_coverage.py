"""st31: 베이즈 신용구간의 빈도 포함률. 이항 n=20, 95% 등꼬리 구간. 사전: 균등, 제프리스, 강한 사전 Beta(20,20). 참 p마다 정확한 포함률."""
import numpy as np
from scipy import stats
n = 20; ks = np.arange(n+1)
for name, a, b in [('균등', 1, 1), ('제프리스', .5, .5), ('강한 사전 Beta(20,20)', 20, 20)]:
    lo = stats.beta.ppf(.025, a+ks, b+n-ks); hi = stats.beta.ppf(.975, a+ks, b+n-ks)
    row = []
    for p in [0.05, 0.2, 0.5, 0.8, 0.95]:
        pm = stats.binom.pmf(ks, n, p); row.append(np.sum(pm[(lo <= p) & (p <= hi)]))
    print(f'{name:20}', ' '.join(f'{v:.3f}' for v in row))

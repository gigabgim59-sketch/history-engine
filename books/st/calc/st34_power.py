"""st34: 두 집단 t 검정(집단마다 n=20, 양측 5%)의 검정력. 효과 크기 d=0.2, 0.5, 0.8(코언의 작은·중간·큰). 그리고 d=0.5에서 검정력 0.8에 필요한 집단당 n."""
from scipy import stats
import numpy as np
def power(d, n):
    df = 2*n-2; nc = d*np.sqrt(n/2); c = stats.t.ppf(.975, df)
    return stats.nct.sf(c, df, nc) + stats.nct.cdf(-c, df, nc)
for d in [0.2, 0.5, 0.8]:
    print(f'd={d}: n=20 검정력 {power(d,20):.3f}')
n = 2
while power(0.5, n) < 0.8: n += 1
print('d=0.5, 검정력 0.8에 필요한 집단당 n =', n)

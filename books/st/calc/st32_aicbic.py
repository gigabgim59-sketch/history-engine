"""st32: 같은 자료에서 AIC와 BIC가 다른 차수를 고른다. 참 모형: y = 1 + 0.5x + 0.3x² + 0.08x³ + N(0,1), x~U(-2,2).
후보: 1~5차 다항식. 모의 2000번에서 고른 차수의 비율."""
import numpy as np
rng = np.random.default_rng(32)
def fit(x, y, d):
    X = np.vander(x, d+1); beta, *_ = np.linalg.lstsq(X, y, rcond=None); r = y - X@beta
    n = len(y); s2 = r@r/n; ll = -n/2*(np.log(2*np.pi*s2)+1); k = d+2
    return -2*ll+2*k, -2*ll+k*np.log(n)
for n in [30, 200, 2000]:
    ca, cb = np.zeros(6), np.zeros(6)
    for _ in range(2000):
        x = rng.uniform(-2, 2, n); y = 1+.5*x+.3*x**2+.08*x**3+rng.normal(0, 1, n)
        A, Bc = zip(*[fit(x, y, d) for d in range(1, 6)]); ca[1+int(np.argmin(A))] += 1; cb[1+int(np.argmin(Bc))] += 1
    print(f'n={n:>4} AIC 1~5차 비율', ' '.join(f'{v/2000:.2f}' for v in ca[1:]), ' | BIC', ' '.join(f'{v/2000:.2f}' for v in cb[1:]))

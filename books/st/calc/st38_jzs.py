"""st38: 라우더 외(2009)의 JZS 베이즈 인자(한 표본 t 검정, 효과 크기에 척도 r=1의 코시 사전). B10 = ∫(1+n g r²)^{-1/2}(1+t²/((1+n g r²)ν))^{-(ν+1)/2} π(g)dg / (1+t²/ν)^{-(ν+1)/2}, g~역감마(1/2,1/2).
t=2.2를 고정하고 n을 바꾸어 양측 p값과 견준다."""
import numpy as np
from scipy import integrate, stats
def B10(t, n, r=1.0):
    nu = n - 1
    f = lambda g: (1+n*g*r*r)**-.5 * (1+t*t/((1+n*g*r*r)*nu))**(-(nu+1)/2) * (2*np.pi)**-.5 * g**-1.5 * np.exp(-1/(2*g))
    num = integrate.quad(f, 0, np.inf, limit=200)[0]
    return num / (1+t*t/nu)**(-(nu+1)/2)
for n in [20, 50, 200, 1000, 10000]:
    b = B10(2.2, n); print(f'n={n:>5}: p={2*stats.t.sf(2.2, n-1):.4f}  B10={b:.2f}  B01={1/b:.2f}')

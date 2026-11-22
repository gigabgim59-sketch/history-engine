"""st24: 부적절 사전의 두 문제. (1) 홀데인 사전 Beta(0,0)에서 n번 모두 실패하면 사후 Beta(0,n)은 적분이 무한 → 사후가 정의되지 않는다.
(2) 점 귀무가설 검정에서 대립가설에 부적절 사전 c·dθ(평평)를 두면 베이즈 인자가 임의의 상수 c에 비례한다.
정규 평균, σ=1, n=10, 관측 평균 0.6(z≈1.90). B01 = φ(z)√n... 를 c마다."""
import numpy as np
from scipy import stats, integrate
for n in [5, 20]:
    val = integrate.quad(lambda p: p**(-1) * (1-p)**(n-1), 1e-12, 1, limit=200)[0]
    val2 = integrate.quad(lambda p: p**(-1) * (1-p)**(n-1), 1e-6, 1, limit=200)[0]
    print(f'모두 실패 n={n}: 하한 1e-12까지 적분 {val:.1f}, 1e-6까지 {val2:.1f} (하한을 0으로 보내면 발산)')
n, xbar = 10, 0.6; se = 1/np.sqrt(n)
f0 = stats.norm.pdf(xbar, 0, se)
m1 = 1.0  # ∫ N(xbar; θ, se) dθ = 1 (평평한 밀도 1에 대해)
for c in [0.1, 1, 10]:
    B = f0 / (c * m1); print(f'평평 사전의 상수 c={c}: B01={B:.3f}')

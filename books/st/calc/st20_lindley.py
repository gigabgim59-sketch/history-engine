"""st20 '같은 자료, 다른 셈' 표 1: p=0.05(양측, z=1.96)에 고정한 자료의 귀무가설 사후 확률이 표본 크기 n에 따라 어떻게 바뀌나.
모형: x_i ~ N(theta, sigma^2), sigma 알려짐. H0: theta=0, 사전 확률 1/2. H1에서 theta ~ N(0, sigma^2)(단위 정보 사전).
베이즈 인자 B01 = sqrt(1+n) * exp(-(z^2/2) * n/(n+1)).  P(H0|x) = B01/(1+B01)."""
import math
z = 1.959963985
print('n, B01, P(H0|x)')
for n in [10, 100, 1000, 10_000, 100_000, 1_000_000]:
    B = math.sqrt(1 + n) * math.exp(-(z * z / 2) * n / (n + 1))
    print(f'{n:>9,}  {B:8.3f}  {B/(1+B):.3f}')
# 바틀릿(1957)의 지적: n을 고정하고 사전의 퍼짐(tau/sigma)을 키우면 같은 일이 일어난다
print('n=100 고정, tau/sigma, P(H0|x)')
for r in [0.1, 1, 10, 100]:
    v = n_ = 100
    t2 = r * r
    B = math.sqrt(1 + n_ * t2) * math.exp(-(z * z / 2) * n_ * t2 / (1 + n_ * t2))
    print(f'{r:>6}  {B/(1+B):.3f}')

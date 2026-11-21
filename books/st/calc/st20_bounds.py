"""st20 표 2: p=0.05(z=1.96)일 때 H1의 사전 분포를 어떤 집합 안에서 마음대로 골라도 P(H0|x)가 내려갈 수 있는 하한.
H0 사전 확률 1/2, 정규 평균, 점 귀무가설. 버거·셀크(1987)가 다룬 사전 집합을 다시 셈한다.
 - 모든 분포: 질량을 관측값 자리 하나에 둔다 → B ≥ exp(-z^2/2)
 - 대칭 분포(0 중심): ±a 두 점 → B(a) = exp(-z^2/2)... 최소를 수치로
 - 대칭 단봉 분포: 0 중심 균등분포 U(-K,K) → 수치 최소
 - 정규 분포 N(0, tau^2): 닫힌 꼴 r=z^2-1에서 B = z*exp(-(z^2-1)/2)
(모수는 표준화: 관측 통계량 z, 표본 평균 표준오차 1)"""
import math
from scipy import optimize, stats
z = 1.959963985
phi = stats.norm.pdf
f0 = phi(z)
P = lambda B: B / (1 + B)
B_all = f0 / phi(0)
B_sym = min(f0 / (0.5 * (phi(z - a) + phi(z + a))) for a in [i / 1000 for i in range(1, 8000)])
def B_uni(K):
    m = (stats.norm.cdf(K - z) - stats.norm.cdf(-K - z)) / (2 * K)
    return f0 / m
B_us = optimize.minimize_scalar(B_uni, bounds=(0.01, 20), method='bounded').fun
B_norm = z * math.exp(-(z * z - 1) / 2)
for name, B in [('모든 분포', B_all), ('대칭', B_sym), ('대칭 단봉', B_us), ('정규', B_norm)]:
    print(f'{name:6}  B01≥{B:.3f}  P(H0|x)≥{P(B):.3f}')

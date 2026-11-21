"""st21: 로열의 가능도비 기준과 오도하는 증거. 단순 가설 둘, 정규 평균(분산 1), 두 평균의 차를 표준오차 단위로 Δ.
H0가 참일 때 가능도비 L1/L0 ≥ k일 확률 = Φ(-Δ/2 - ln k/Δ). Δ에 대한 최댓값 Φ(-√(2 ln k)). 일반 상한 1/k."""
from math import log, sqrt
from scipy.stats import norm
for k in [8, 32]:
    row = [norm.cdf(-d/2 - log(k)/d) for d in [0.5, 1, 2, 3, 4, 6]]
    print(f'k={k}: Δ=0.5,1,2,3,4,6 →', ' '.join(f'{v:.4f}' for v in row), f' 최댓값 {norm.cdf(-sqrt(2*log(k))):.4f}  상한 1/k={1/k:.4f}')

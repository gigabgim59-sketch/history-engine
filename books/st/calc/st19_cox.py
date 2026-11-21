"""st19: 콕스(1958)의 두 측정기. 동전으로 측정기를 고른다: 정밀(σ=1) 또는 거친(σ=10), 각 1/2.
H0: μ=0 대 H1: μ=5, 관측 하나, 한쪽 검정, 전체 수준 5%.
(가) 조건부 검정: 고른 측정기 안에서 각각 5%. (나) 무조건 최강 검정: 두 측정기의 1종 오류 α1, α2를 평균 0.05로 묶고
전체 검정력이 가장 크게 나눈다(격자 탐색)."""
import numpy as np
from scipy.stats import norm as N
mu = 5
P = lambda a: 0.5 * N.sf(N.isf(a) - mu) + 0.5 * N.sf(N.isf(0.1 - a) - mu / 10)
grid = np.linspace(1e-5, 0.09999, 20000); a1 = grid[np.argmax([P(a) for a in grid])]; a2 = 0.1 - a1
print(f'조건부: α 정밀 0.050, 거친 0.050 | 검정력 정밀 {N.sf(N.isf(.05)-mu):.3f}, 거친 {N.sf(N.isf(.05)-mu/10):.3f}, 전체 {P(0.05):.3f}')
print(f'무조건 최강: α 정밀 {a1:.4f}, 거친 {a2:.4f} | 검정력 정밀 {N.sf(N.isf(a1)-mu):.3f}, 거친 {N.sf(N.isf(a2)-mu/10):.3f}, 전체 {P(a1):.3f}')

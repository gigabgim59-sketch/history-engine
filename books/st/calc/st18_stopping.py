"""st18 '같은 자료, 다른 셈'.
표 1: 린들리·필립스(1976)의 예. 앞면 9, 뒷면 3. 설계 A(12번 던지기로 정함, 이항), 설계 B(뒷면 3번이 나오면 멈춤, 음이항).
 H0: theta=1/2 대 theta>1/2의 한쪽 p값. 가능도는 두 설계 모두 theta^9 (1-theta)^3에 비례.
표 2: 귀무가설이 참일 때 자료가 쌓일 때마다 양측 5% 검정(|z|>1.96)을 되풀이하면, 한 번이라도 '유의'가 나올 확률.
 같은 간격으로 k번 들여다본다(정규 증분, 분산 알려짐). 수치 적분(격자 위 밀도 전파)으로 셈하고 몬테카를로로 대조한다."""
from math import comb
import numpy as np
pA = sum(comb(12, k) for k in range(9, 13)) / 2 ** 12
pB = 1 - sum(comb(k + 2, 2) * 0.5 ** (k + 3) for k in range(0, 9))
print(f'이항 p={pA:.4f}  음이항 p={pB:.4f}')
# 사후: 균등 사전이면 두 설계 모두 Beta(10,4). P(theta>1/2 | x)
from scipy import stats
print('사후 P(theta>1/2)=', round(1 - stats.beta(10, 4).cdf(0.5), 4))

c = 1.959963985
L = 30.0; h = 0.005  # 격자 끝(L)은 c*sqrt(50)≈13.9보다 넉넉히
x = np.arange(-L, L + h, h)
def looks(K):
    # S_k = 증분 합(분산 1씩). 거절 조건 |S_k| > c*sqrt(k)
    dens = np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)  # S_1
    rej = 0.0
    ker = np.exp(-np.arange(-6, 6 + h, h) ** 2 / 2) / np.sqrt(2 * np.pi) * h
    for k in range(1, K + 1):
        if k > 1:
            dens = np.convolve(dens, ker, mode='same')
        out = np.abs(x) > c * np.sqrt(k)
        rej += dens[out].sum() * h
        dens = np.where(out, 0, dens)
    return rej
rng = np.random.default_rng(1)
for K in [1, 2, 3, 5, 10, 20, 50]:
    S = np.cumsum(rng.standard_normal((200_000, K)), axis=1)
    mc = (np.abs(S) > c * np.sqrt(np.arange(1, K + 1))).any(axis=1).mean()
    print(f'{K:>3}번  수치 {looks(K):.3f}  몬테카를로 {mc:.3f}')

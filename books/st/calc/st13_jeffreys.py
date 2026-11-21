"""st13: 제프리스식 검정과 유의성 검정. 동전 n번 중 k번 앞면. H0: p=1/2(사전 확률 1/2), H1: p~균등(0,1).
B01 = C(n,k)(1/2)^n / (1/(n+1)). 양측 p값(정확 이항)과 나란히."""
from math import comb, lgamma, log, exp
from scipy import stats
for n, k in [(20, 15), (100, 60), (1000, 532), (10000, 5098)]:
    B = exp(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1) + n*log(0.5) + log(n+1))
    p = stats.binomtest(k, n, 0.5).pvalue
    print(f'n={n:>5} k={k:>5}: 양측 p={p:.4f}  B01={B:.3f}  P(H0|x)={B/(1+B):.3f}')
# 대립가설 사전을 0.5 근처에 모은 경우(Beta(10,10))와 넓힌 경우(균등) — n=100, k=60
from scipy.special import betaln
n, k = 100, 60
for a in [1, 10, 50]:
    lB = n*log(0.5) - (betaln(k+a, n-k+a) - betaln(a, a))
    B = exp(lB); print(f'대립 사전 Beta({a},{a}): B01={B:.3f} P(H0|x)={B/(1+B):.3f}')

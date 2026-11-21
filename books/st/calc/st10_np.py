"""st10: 같은 자료, 피셔식 보고와 네이만–피어슨식 결정.
정규 평균, σ=1, n=25, H0: μ=0 대 H1: μ=0.5. 한쪽 검정. 관측 평균 0.38.
피셔: p값. NP: α=0.05의 기각역 x̄>1.645/5=0.329, 검정력, 2종 오류."""
from scipy import stats
n, s = 25, 1; se = s / n ** 0.5; xbar = 0.38
p = stats.norm.sf(xbar / se); c = stats.norm.isf(0.05) * se
for mu1 in [0.3, 0.5, 0.7]:
    print(f'μ1={mu1}: 검정력 {stats.norm.sf((c-mu1)/se):.3f}  2종 오류 {stats.norm.cdf((c-mu1)/se):.3f}')
print(f'p={p:.4f}  기각역 x̄>{c:.3f}  결정: {"기각" if xbar>c else "채택"}')
for x in [0.33, 0.38, 0.50, 0.70]:
    print(f'x̄={x}: p={stats.norm.sf(x/se):.4f}  NP 결정 {"기각" if x>c else "채택"}  가능도비 L1/L0(μ1=0.5)={stats.norm.pdf((x-0.5)/se)/stats.norm.pdf(x/se):.2f}')

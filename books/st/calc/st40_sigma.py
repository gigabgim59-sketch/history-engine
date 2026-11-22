"""st40: 시그마와 p값(한쪽), 그리고 '다른 곳을 본 효과': 질량 구간 N개를 함께 볼 때 국소 p가 전체에서 우연히 나올 확률 1-(1-p)^N."""
from scipy import stats
for s in [2, 3, 4, 5]:
    p = stats.norm.sf(s); print(f'{s}σ: 한쪽 p={p:.3g} (약 {1/p:,.0f}분의 1)')
for N in [10, 100, 1000]:
    for s in [3, 5]:
        p = stats.norm.sf(s); print(f'  구간 {N}개, 국소 {s}σ → 전체 p≈{1-(1-p)**N:.3g}')

"""st09: 피셔(1935)의 차 맛보기. 8잔(우유 먼저 4, 차 먼저 4), 4잔을 고르게 한다.
모두 맞힐 확률 1/C(8,4)=1/70. 3잔 이상 맞힐 확률 (1+16)/70. 그리고 K. 피어슨의 카이제곱 예: 주사위 600번."""
from math import comb
from scipy import stats
tot = comb(8, 4)
for k in range(5):
    print(f'{k}잔 맞힘: {comb(4,k)*comb(4,4-k)}/70')
print('4잔 모두 p=', round(1/tot, 4), ' 3잔 이상 p=', round((1+16)/tot, 4))
obs = [90, 95, 100, 105, 110, 100]; exp = [100]*6
c2 = sum((o-e)**2/e for o, e in zip(obs, exp)); print('카이제곱', c2, 'p=', round(stats.chi2.sf(c2, 5), 3))
obs2 = [80, 95, 100, 105, 110, 110]; c2b = sum((o-e)**2/e for o, e in zip(obs2, exp)); print('카이제곱', c2b, 'p=', round(stats.chi2.sf(c2b, 5), 4))

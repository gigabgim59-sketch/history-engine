"""st15: 발트의 위험 함수. 이항 n=20, 제곱 손실로 p를 추정하는 세 규칙의 위험 E[(d-p)^2]를 p마다 셈한다.
최대가능도 x/n, 균등 사전의 베이즈 (x+1)/(n+2), 최소최대 (x+√n/2)/(n+√n)(위험이 p와 상관없이 일정)."""
import numpy as np
from scipy import stats
n = 20; x = np.arange(n + 1)
rules = {'최대가능도 x/n': x / n, '베이즈(균등) (x+1)/(n+2)': (x + 1) / (n + 2), '최소최대': (x + n ** .5 / 2) / (n + n ** .5)}
ps = [0.05, 0.2, 0.5, 0.8, 0.95]
for name, d in rules.items():
    r = [np.sum(stats.binom.pmf(x, n, p) * (d - p) ** 2) for p in ps]
    print(f'{name:24}', ' '.join(f'{v:.4f}' for v in r), ' 최대', round(max(np.sum(stats.binom.pmf(x, n, p) * (d - p) ** 2) for p in np.linspace(0, 1, 201)), 4))

"""st39: 메이오의 엄격성. 정규 평균, σ/√n=0.2, 관측 평균 0.4(H0: μ≤0 기각, z=2). 주장 'μ>μ1'의 엄격성 SEV = P(X̄ ≤ 0.4; μ=μ1).
평평한 사전의 사후 확률 P(μ>μ1 | x)와 견준다(이 경우 숫자가 같다)."""
from scipy import stats
for m1 in [0, 0.2, 0.4, 0.6, 0.8]:
    sev = stats.norm.cdf((0.4-m1)/0.2); post = 1-stats.norm.cdf(m1, 0.4, 0.2)
    print(f'μ>{m1}: 엄격성 {sev:.3f}  평평한 사전의 사후 {post:.3f}')

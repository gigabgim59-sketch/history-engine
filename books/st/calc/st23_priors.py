"""st23: 10번 중 7번 성공. 네 사전의 사후: 균등 Beta(1,1), 제프리스 Beta(1/2,1/2), 홀데인 Beta(0,0)(부적절), 주관적 Beta(20,20)(p가 1/2 근처라고 믿는 사람).
그리고 제프리스 사전의 불변성: 로그 오즈로 바꿔도 같은 사후를 준다(p 위에서 셈한 사후 구간과 φ 위에서 셈해 되돌린 구간이 같다)."""
import numpy as np
from scipy import stats
for name, a, b in [('균등', 1, 1), ('제프리스', .5, .5), ('홀데인(부적절)', 0, 0), ('주관 Beta(20,20)', 20, 20)]:
    d = stats.beta(a + 7, b + 3); lo, hi = d.ppf([.025, .975])
    print(f'{name:14} 사후 평균 {d.mean():.3f}  95% {lo:.3f}–{hi:.3f}  P(p>0.5) {1-d.cdf(.5):.3f}')
# 불변성 확인: φ=logit p, 제프리스 사전은 φ 위에서 √I(φ)=√(p(1-p)) → p 위로 바꾸면 Beta(1/2,1/2)
phi = np.linspace(-12, 12, 400001); p = 1/(1+np.exp(-phi))
post = np.sqrt(p*(1-p)) * p**7 * (1-p)**3; post /= post.sum()
c = np.cumsum(post); lo, hi = p[np.searchsorted(c, .025)], p[np.searchsorted(c, .975)]
print(f'φ 위에서 제프리스 사전으로 셈해 p로 되돌린 95% 구간 {lo:.3f}–{hi:.3f}')
print('10번 중 0번 성공:')
for name, a, b in [('균등', 1, 1), ('제프리스', .5, .5)]:
    d = stats.beta(a, b + 10); print(f'  {name}: 평균 {d.mean():.3f}  95% 상한 {d.ppf(.95):.3f}')
print('  홀데인: Beta(0,10) — 적분이 발산해 사후가 정의되지 않음')

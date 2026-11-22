"""st37: 문턱 0.05와 0.005. (1) 양측 검정에서 검정력 0.8을 지키려면 표본이 몇 배 필요한가: ((z_{α/2}+z_{0.2})/(1.96+z_{0.2}))^2.
(2) 사전 승산 R=1/10, 검정력 0.8일 때 유의한 발견이 참일 확률. (3) p값의 베이즈 인자 하한 1/(-e p ln p)(대립 쪽)."""
from scipy import stats
import math
zb = stats.norm.isf(0.2)
for a in [0.05, 0.005]:
    za = stats.norm.isf(a/2); ratio = ((za+zb)/(stats.norm.isf(.025)+zb))**2
    ppv = 0.8*0.1/(0.8*0.1+a)
    bf = 1/(-math.e*a*math.log(a))
    print(f'α={a}: 표본 배수 {ratio:.2f}, PPV(R=0.1) {ppv:.2f}, p=α일 때 대립 쪽 베이즈 인자 상한 {bf:.1f}')

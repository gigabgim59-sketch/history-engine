"""st27: 같은 최종 자료, 다른 의도. 정규 자료 n=100에서 최종 z=2.00.
(가) 처음부터 100개로 정한 설계: 양측 p=0.0455 → 5%에서 유의.
(나) 50개에서 한 번 들여다보고 계속하는 2단계 설계(포콕식 같은 경계로 전체 5%): 경계 c를 찾고 최종 z=2.00과 견준다.
(다) 의도만 달랐고 실제로는 중간에 들여다보지 않았어도, 빈도 쪽의 오류율 셈은 설계를 따른다. 가능도와 사후 분포는 두 경우 같다."""
import numpy as np
from scipy import stats, optimize
rho = np.sqrt(0.5)
def level(c):
    cov = [[1, rho], [rho, 1]]
    p_in = stats.multivariate_normal(mean=[0, 0], cov=cov).cdf([c, c]) - stats.multivariate_normal(mean=[0, 0], cov=cov).cdf([-c, c]) \
         - stats.multivariate_normal(mean=[0, 0], cov=cov).cdf([c, -c]) + stats.multivariate_normal(mean=[0, 0], cov=cov).cdf([-c, -c])
    return 1 - p_in
c = optimize.brentq(lambda c: level(c) - 0.05, 1.5, 3)
print(f'고정 설계: p={2*stats.norm.sf(2.0):.4f}, 경계 1.960')
print(f'2단계 포콕식: 경계 {c:.3f} (단계마다 명목 수준 {2*stats.norm.sf(c):.4f}), 최종 z=2.00은 {"유의" if 2.0>c else "유의하지 않음"}')

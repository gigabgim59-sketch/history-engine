"""st20 표 3: 셀크·바야리·버거(2001)의 보정 -e p ln p(p<1/e)와, 점 귀무가설 정규 검정에서 버거·셀크(1987)식 하한을 p=0.05, 0.01, 0.005에서 견준다.
H0 사전 확률 1/2. P(H0|x)의 하한 = B/(1+B)."""
import math
from scipy import stats
for p in [0.05, 0.01, 0.005]:
    z = stats.norm.isf(p / 2)
    B_all = math.exp(-z * z / 2)
    B_norm = z * math.exp(-(z * z - 1) / 2)
    B_cal = -math.e * p * math.log(p)
    f = lambda B: B / (1 + B)
    print(f'p={p}: z={z:.3f}  모든분포 {B_all:.3f}/{f(B_all):.3f}  정규 {B_norm:.3f}/{f(B_norm):.3f}  -e p ln p {B_cal:.3f}/{f(B_cal):.3f}')

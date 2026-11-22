"""st35: (1) 독립 검정 m개를 각각 5%로 하면 적어도 하나 거짓 양성일 확률 1-0.95^m.
(2) 1,000개 가설 가운데 100개에 효과(z 평균 3). 보정 없음, 본페로니, 벤야미니–호흐베르크(FDR 5%)의 거짓 발견 비율과 검정력(500번 모의)."""
import numpy as np
from scipy import stats
for m in [1, 5, 20, 100]:
    print(f'm={m}: {1-0.95**m:.3f}')
rng = np.random.default_rng(35); m, k = 1000, 100; R = 500
res = {'보정 없음': [], '본페로니': [], 'BH': []}
for _ in range(R):
    z = rng.normal(0, 1, m); z[:k] += 3; p = 2*stats.norm.sf(np.abs(z)); truth = np.arange(m) < k
    rej = {'보정 없음': p < .05, '본페로니': p < .05/m}
    o = np.argsort(p); ok = p[o] <= .05*np.arange(1, m+1)/m; kmax = np.max(np.where(ok)[0])+1 if ok.any() else 0
    r = np.zeros(m, bool); r[o[:kmax]] = True; rej['BH'] = r
    for name, r in rej.items():
        nr = r.sum(); res[name].append(((r & ~truth).sum()/max(nr, 1), (r & truth).sum()/k))
for name, v in res.items():
    v = np.array(v); print(f'{name:6} 거짓 발견 비율 {v[:,0].mean():.3f}  검정력 {v[:,1].mean():.3f}')

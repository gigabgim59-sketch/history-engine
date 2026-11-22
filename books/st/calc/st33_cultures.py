"""st33: 같은 자료에 두 문화. 가상 자료 y = sin(2x1) + x2² + 0.5·x1·x2 + N(0, 0.3²), x~U(-2,2)², 학습 400·시험 2000.
(가) 선형 회귀: 계수와 그 해석. (나) k-최근접 이웃(k=10): 계수 없음. 시험 자료의 평균 제곱 예측 오차를 견준다."""
import numpy as np
rng = np.random.default_rng(33)
def gen(n):
    X = rng.uniform(-2, 2, (n, 2)); y = np.sin(2*X[:,0]) + X[:,1]**2 + 0.5*X[:,0]*X[:,1] + rng.normal(0, .3, n); return X, y
Xtr, ytr = gen(400); Xte, yte = gen(2000)
A = np.c_[np.ones(400), Xtr]; b, *_ = np.linalg.lstsq(A, ytr, rcond=None)
mse_lin = np.mean((np.c_[np.ones(2000), Xte]@b - yte)**2)
d = ((Xte[:, None, :] - Xtr[None, :, :])**2).sum(-1); idx = np.argsort(d, 1)[:, :10]
mse_knn = np.mean((ytr[idx].mean(1) - yte)**2)
print(f'선형 회귀 계수 {np.round(b,3)}, 시험 오차 {mse_lin:.3f}; k-최근접 이웃 시험 오차 {mse_knn:.3f}; 잡음 분산 {0.09:.3f}')

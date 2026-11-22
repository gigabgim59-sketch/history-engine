"""st25: 제임스–스타인. k개의 정규 평균 θ_i, 관측 x_i ~ N(θ_i, 1). 총 제곱 오차의 기댓값: 최대가능도(x 그대로) = k.
제임스–스타인 (1-(k-2)/|x|^2) x 는 k≥3에서 모든 θ에 대해 더 작다. θ를 바꿔 가며 모의.
그리고 경험적 베이즈 읽기: θ_i ~ N(0, τ²)이면 베이즈 규칙은 (1-1/(1+τ²))x, 그 축소량을 자료에서 추정한 것이 제임스–스타인."""
import numpy as np
rng = np.random.default_rng(25); R = 20000
for k in [3, 10, 50]:
    for spread in [0, 1, 3]:
        th = rng.normal(0, spread, k) if spread else np.zeros(k)
        x = th + rng.standard_normal((R, k))
        js = (1 - (k-2) / np.sum(x**2, 1, keepdims=True)) * x
        print(f'k={k:>2} θ퍼짐={spread}: 최대가능도 {np.mean(np.sum((x-th)**2,1)):.2f}  제임스–스타인 {np.mean(np.sum((js-th)**2,1)):.2f}')

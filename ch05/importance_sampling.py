"""重点サンプリング　p.162"""


import numpy as np


x = np.array([1, 2, 3])
pi = np.array([0.1, 0.1, 0.8])

# 定義式による期待値
e = np.sum(x * pi)
print('E_pi[x]', e)

# モンテカルロ法
n = 100
samples = []
for _ in range(n):
    s = np.random.choice(x, p=pi)
    samples.append(s)

mean = np.mean(samples)
var = np.var(samples)
print(f'MC: {mean:.2f}, var: {var:.2f}')

# 重点サンプリング
# b = np.array([1/3, 1/3, 1/3])
b = np.array([0.2, 0.2, 0.6])
samples = []

for _ in range(n):
    idx = np.arange(len(b))
    i = np.random.choice(idx, p=b)
    s = x[i]
    rho = pi[i] / b[i]
    samples.append(rho * s)

mean = np.mean(samples)
var = np.var(samples)
print(f'IS: {mean: .2f}, var: {var: .2f}')
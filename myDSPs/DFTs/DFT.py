import numpy as np

x = np.array([0, 1, 2, 3])

N = np.size(x)
X = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        X[k] = X[k] + x[n] * np.exp(-2j * np.pi * k * n / N)

print('x=', x)
print('X=', X)

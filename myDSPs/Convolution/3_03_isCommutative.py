import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

N = 20
# x = np.random.rand(1, N)
x = np.random.rand(N, 1)
y = np.random.rand(N, 1)
z3 = sp.convolve(x, y)
z4 = sp.convolve(y, x)

print(all(z3 == z4))
print(z3 == z4)

plt.plot(z3, 'o', label='z3')
plt.plot(z4, 'x', label='z4')
plt.legend()
plt.title('Comparison of z3 and z4')
plt.show()

print(np.allclose(z3, z4))

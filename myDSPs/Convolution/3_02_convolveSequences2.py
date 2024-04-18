import numpy as np
import scipy.signal as sp

x = [1, 2, 0, 3]
y = [2, 0, 3, 1]

z1 = np.convolve(x, y)
z2 = sp.convolve(x, y)

print(z1)
print(z2)


import numpy as np
import scipy.signal as sp

# y[n] = x[n] + 2*y[n-1]
b = np.array([1])
a = np.array([1, -2])

x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]).astype('float')

y = sp.lfilter(b, a, x)

print(y)

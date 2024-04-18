import numpy as np
import scipy.signal as sp

# y[n] = x[n] + 2*x[n-1] - x[n-2] - y[n-1] + y[n-2]
b = np.array([1, 2, -1])
a = np.array([1, -1, 1])

x = np.array([1, 0, 2]).astype('float')

y = sp.lfilter(b, a, x)

print(y)

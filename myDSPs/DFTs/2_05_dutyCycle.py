import numpy as np
import matplotlib.pyplot as plt

def mySquarePeriodical(A, f, ph0, n, t):
    x = np.zeros(np.size(t))
    for k in range(n):
        xt = ((4 / np.pi) / (2 * k + 1)) * np.sin(2 * np.pi * (2 * k + 1) * f * t + ph0)
        x = x + xt
    return x

# create time vector
fs = 1000
t0 = 0
t1 = 3
t = np.arange(t0, t1, 1 / fs)

A = 1
f = 1
ph0 = np.pi
n = 4

plt.close('all')
x = mySquarePeriodical(A, f, ph0, n, t)
plt.plot(t, x)
plt.grid(True)
plt.show()


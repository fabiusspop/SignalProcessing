import myDSP
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

t0 = 0
t1 = 1
fs = 44100
t = np.arange(t0, t1, 1 / fs)

A = 1
f = 440
# f = 15000
x = myDSP.mySine(A, f, 0, t)

plt.close('all')
plt.plot(t, x)
plt.axis([0, 5 * 10**-3, -1, 1])
plt.grid()
sd.play(x, fs)
print('ok')
plt.show()

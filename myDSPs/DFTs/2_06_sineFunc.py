import numpy as np
import matplotlib.pyplot as plt
import myDSP

t0 = 1
t1 = 2
fs = 200
t = np.arange(t0, t1 + 1 / fs, 1 / fs)

f = 16
x = myDSP.mySine(1, f, 0, t)

plt.close('all')

plt.plot(t, x)
myDSP.plotInTime(x, fs)
myDSP.plotInFrequency(x, fs)

plt.show()
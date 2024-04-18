import numpy as np
import matplotlib.pyplot as plt
import myDSP

t0 = 0
t1 = 5
fs = 100
t = np.arange(t0, t1 + 1/fs, 1/fs)

plt.close('all')

y = myDSP.myCosine(2, 1, 0, t)
plt.plot(t, y)
plt.grid(True)

y = myDSP.myRamp(3, 2, t)
plt.plot(t, y)

y = myDSP.myBox(1, 1, 3, t)
plt.plot(t, y)

y = myDSP.myWhiteNoise(0.5, t)
plt.plot(t, y)
plt.show()

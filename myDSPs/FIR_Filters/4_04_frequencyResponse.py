import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

x = np.arange(-10, 10.1, 0.5)
b = np.sinc(x)

plt.figure()

a = np.array([1.])

w, H = sp.freqz(b, a, worN=512, whole=False)
f = w / np.pi

plt.subplot(1, 2, 1)
plt.plot(b, '.-')
plt.title('Filter Coefficients')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(f, abs(H), '.-')
plt.title('Transfer Function')
plt.xlabel('Normalized Frequency (x π rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

w = 0.75

N = 9

b = sp.firwin(N, w)
a = np.array([1.])

w, H = sp.freqz(b, a, worN=512, whole=False)
f = w / np.pi

plt.figure()

plt.subplot(1, 2, 1)
plt.plot(b, '.-')
plt.title('Filter Coefficients')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(f, abs(H))
plt.title('Frequency Response')
plt.xlabel('Normalized Frequency (x π rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)

print(np.round(100 * b))

plt.show()

import numpy as np
import scipy.signal as dsp
import matplotlib.pyplot as plt

N = 64
x = np.random.randint(N, size=N) - N / 2
y = np.random.randint(N, size=N) - N / 2
z = dsp.convolve(x, y)

plt.close('all')

plt.subplot(3, 2, 1)
plt.plot(x, 'b.-')
plt.title('x')

plt.subplot(3, 2, 3)
plt.plot(y, 'r.-')
plt.title('y')

plt.subplot(3, 2, 5)
plt.plot(z, 'g.-')
plt.title('x*y')

x = np.pad(x, (0, len(z) - len(x)), 'constant')
y = np.pad(y, (0, len(z) - len(y)), 'constant')

X = np.fft.fft(x)
Y = np.fft.fft(y)
Z = np.fft.fft(z)

plt.subplot(3, 2, 2)
plt.plot(abs(X), 'b.-')
plt.title('X=DFT(x)')

plt.subplot(3, 2, 4)
plt.plot(abs(Y), 'r.-')
plt.title('Y=DFT(y)')

plt.subplot(3, 2, 6)
plt.plot(abs(Z), 'g.-')
plt.title('Z=DFT(x*y)')

ZZ = X * Y
plt.subplot(3, 2, 6)
plt.plot(abs(ZZ), 'md')
plt.title('DFT(x*y) and XY')

plt.tight_layout()
plt.show()

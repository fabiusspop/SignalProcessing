import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.1, 0.5)
h = np.sinc(x)

plt.close('all')

plt.subplot(2, 2, 1)
plt.plot(x, h, '.-')
plt.title('Cardinal Sinus in Time')
plt.grid(True)

H = np.fft.fft(h)
plt.subplot(2, 2, 2)
plt.plot(np.fft.fftshift(abs(H)), '.-')
plt.title('Fourier Transform')
plt.grid(True)

plt.subplot(2, 2, 4)
N = int(len(H) / 2)
plt.plot(np.fft.fftfreq(len(H), d=(x[1] - x[0]))[:N], abs(H)[:N], '.-')
plt.title('Halfband for the Fourier Transform')
plt.grid(True)

plt.tight_layout()
plt.show()

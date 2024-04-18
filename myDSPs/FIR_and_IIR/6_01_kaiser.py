import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

fs = 44100

fc = np.array([7000, 12000])

ft = 1000
w = fc / (fs / 2)
wt = ft / (fs / 2)

r = 40

N, beta = sp.kaiserord(r, wt)
print("Filter order:", N)

b = sp.firwin(N, w, window=('kaiser', beta), pass_zero=False)
a = np.array([1.])  # Since it's an FIR filter, the denominator is 1

w, h = sp.freqz(b, a=1, worN=512, whole=False)
f = (fs / 2) * w / np.pi

plt.figure(figsize=(10, 6))
plt.plot(f, abs(h), label='Bandpass Filter')
plt.plot([0, fc[0], fc[0], fc[1], fc[1], fs/2], [0, 0, 1, 1, 0, 0], 'r--', label='Ideal Response')
plt.title('Frequency Response of the Bandpass Filter')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain')
plt.grid(True)
plt.legend()
plt.show()

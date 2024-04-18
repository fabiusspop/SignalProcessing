import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 8000  # Sampling frequency
fc1 = 1000  # Lower cut-off frequency
fc2 = 2000  # Upper cut-off frequency
ft = 400    # Transition band width

rp = 0.2  # Passband ripple in dB
rs = 35   # Stopband attenuation in dB

wp = np.array([fc1 + ft/2, fc2 - ft/2]) / (fs / 2)
ws = np.array([fc1 - ft/2, fc2 + ft/2]) / (fs / 2)

def generalPlot(s):
    plt.plot([fc1 - ft/2, fc2 + ft/2], [0, 0], 'or')  # Stopband edges
    plt.plot([fc1 + ft/2, fc2 - ft/2], [1, 1], 'or')  # Passband edges
    plt.plot([0, fc1, fc1, fc2, fc2, fs/2], [0, 0, 1, 1, 0, 0], 'k', label='Ideal')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Gain')
    plt.title(f'Frequency Response for the {s}')
    plt.legend()
    plt.grid(True)

plt.figure(figsize=[12, 9])

N, wn = sp.cheb1ord(wp, ws, rp, rs)
print(f'Filter order for Chebyshev Type 1 is {N}')
b, a = sp.cheby1(N, rp, wn, btype='bandpass')
w, h = sp.freqz(b, a, worN=512)
f = (fs / 2) * w / np.pi
plt.subplot(2, 2, 1)
plt.plot(f, abs(h), linewidth=2, label='Chebyshev Type 1')
generalPlot('Chebyshev Type 1')

N, wn = sp.cheb2ord(wp, ws, rp, rs)
print(f'Filter order for Chebyshev Type 2 is {N}')
b, a = sp.cheby2(N, rs, wn, btype='bandpass')
w, h = sp.freqz(b, a, worN=512)
f = (fs / 2) * w / np.pi
plt.subplot(2, 2, 2)
plt.plot(f, abs(h), linewidth=2, label='Chebyshev Type 2')
generalPlot('Chebyshev Type 2')

N, wn = sp.buttord(wp, ws, rp, rs)
print(f'Filter order for Butterworth is {N}')
b, a = sp.butter(N, wn, btype='bandpass')
w, h = sp.freqz(b, a, worN=512)
f = (fs / 2) * w / np.pi
plt.subplot(2, 2, 3)
plt.plot(f, abs(h), linewidth=2, label='Butterworth')
generalPlot('Butterworth')

N, wn = sp.ellipord(wp, ws, rp, rs)
print(f'Filter order for Elliptic is {N}')
b, a = sp.ellip(N, rp, rs, wn, btype='bandpass')
w, h = sp.freqz(b, a, worN=512)
f = (fs / 2) * w / np.pi
plt.subplot(2, 2, 4)
plt.plot(f, abs(h), linewidth=2, label='Elliptic')
generalPlot('Elliptic')

plt.tight_layout()
plt.show()

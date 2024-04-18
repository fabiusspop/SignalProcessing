import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 8000  # Sampling frequency in Hz
fc = 2000  # Center frequency in Hz
ft = 400   # Transition width in Hz

rp = 0.1   # Passband ripple in dB
rs = 50    # Stopband attenuation in dB

wp = (fc - ft / 2) / (fs / 2)
ws = (fc + ft / 2) / (fs / 2)

N, wn = sp.cheb1ord(wp, ws, rp, rs)

b, a = sp.cheby1(N, rp, [wp, ws], btype='band')

w, h = sp.freqz(b, a, worN=512)

f = (fs / 2) * w / np.pi

print(f"Filter order: {N}")

plt.close('all')
plt.plot(f, abs(h), linewidth=3, label='Bandpass Filter')
plt.plot([fc - ft / 2, fc + ft / 2], [1, 1], 'or', label='Passband Edges')
plt.axvline(x=fc - ft / 2, color='k', linestyle='--')
plt.axvline(x=fc + ft / 2, color='k', linestyle='--')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain')
plt.title('Frequency Response of Chebyshev Type I Bandpass Filter')
plt.grid(True)
plt.legend()
plt.show()

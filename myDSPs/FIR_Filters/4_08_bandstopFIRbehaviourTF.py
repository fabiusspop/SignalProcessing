import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
import time

# Assuming myDSP module has the necessary functions
import myDSP

w = [0.2, 0.5]
N = 51
fs = 8000

b = sp.firwin(N, w, pass_zero=False)
a = [1.]

w, H = sp.freqz(b, a, worN=512, whole=False)
f_response = (w / np.pi) * (fs / 2)

plt.figure()
plt.plot(f_response, abs(H))
plt.title('Frequency Response of the FIR Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

t = np.arange(0, 1, 1 / fs)

frequency = [440, 1200, 3000]

for f in frequency:
    x = myDSP.mySine(1, f, 0, t)

    print(f'Sound at {f} Hz, original')
    myDSP.play(x, fs)
    time.sleep(2)

    y = sp.lfilter(b, a, x)

    print(f'Sound at {f} Hz, filtered')
    myDSP.play(y, fs)
    input('Press ENTER to continue...')

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.title(f'Original Sine Wave at {f} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plt.plot(t, y)
    plt.title(f'Filtered Sine Wave at {f} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

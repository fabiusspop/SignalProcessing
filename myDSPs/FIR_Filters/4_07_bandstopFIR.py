import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

w = [0.2, 0.5]

filterOrder = [9, 27, 81, 243]

a = np.array([1.])

plt.close('all')

for N in filterOrder:
    b = sp.firwin(N, w, pass_zero=False)

    f, H = sp.freqz(b, a, worN=512, whole=False)
    f = f / np.pi

    F = plt.figure(figsize=(10, 4))
    F.suptitle(f'FIR Band-Pass Filter of Order {N}')

    plt.subplot(1, 2, 1)
    plt.plot(b, '.-')
    plt.title('Filter Coefficients')
    plt.xlabel('Coefficient Index')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(f, abs(H))
    plt.title('Frequency Response')
    plt.xlabel('Normalized Frequency (x π rad/sample)')
    plt.ylabel('Magnitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

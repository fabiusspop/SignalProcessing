import numpy as np
import matplotlib.pyplot as plt
import myDSP

def wavePlot(t, x, s):
    X = abs(np.fft.fft(x))
    fig = plt.figure(figsize=(12, 4))
    fig.suptitle(s, fontsize=16)
    plt.title(s)
    plt.subplot(1, 2, 1)
    plt.plot(t, x)
    plt.xlabel('time(s)')
    plt.ylabel('Amplitude of x')
    plt.title('Time representation')
    plt.grid(True)
    plt.subplot(1, 2, 2)
    plt.plot(X)
    plt.xlabel('index')
    plt.ylabel('Modulus of X')
    plt.title('Frequency representation')
    plt.grid(True)

t0 = 0
t1 = 5
fs = 100
t = np.arange(t0, t1 + 1 / fs, 1 / fs)

plt.close('all')
plt.show()

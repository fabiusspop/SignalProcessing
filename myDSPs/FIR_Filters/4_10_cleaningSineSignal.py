import numpy as np
import myDSP  # Ensure this module has the necessary function mySine
import scipy.signal as sp
import matplotlib.pyplot as plt

# Sampling frequency
fs = 100

# Time vector
t = np.arange(0, 1, 1/fs)

# Close all existing figures
plt.close('all')

# Signal parameters
A = 1  # Amplitude
f = 3  # Frequency in Hz

# Generate sine wave
x = myDSP.mySine(A, f, 0, t)

# Plot original sine wave
plt.subplot(4, 1, 1)
plt.plot(t, x)
plt.title('Original Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Generate zero-centered noise
noise = np.random.rand(np.size(x)) - 0.5

# Plot noise
plt.subplot(4, 1, 2)
plt.plot(t, noise, 'r')
plt.title('Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Add noise to the sine wave
y = x + noise

# Plot noisy signal
plt.subplot(4, 1, 3)
plt.plot(t, y, 'm')
plt.title('Noisy Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

N = 16
h = (1 / N) * np.ones(N)
z = sp.convolve(y, h, 'same')

plt.subplot(4, 1, 4)
plt.plot(t, z, 'g')
plt.title('Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

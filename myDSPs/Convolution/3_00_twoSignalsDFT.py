import numpy as np
import matplotlib.pyplot as plt
import myDSP
import time

def speedUp(N):
    x = np.random.randint(10, size=2**N)
    start = time.time()
    X = myDSP.myDFT(x)
    t1 = time.time() - start
    start = time.time()
    X = np.fft.fft(x)
    t2 = time.time() - start
    if t2 == 0:
        t2 = np.finfo(float).eps
    return t1 / t2

N = np.arange(8, 13)
spUp = np.zeros(len(N))
for index in range(len(N)):
    print(index)
    spUp[index] = speedUp(N[index])

plt.plot(N, spUp, '.-')
plt.xlabel('Power of 2')
plt.ylabel('Speed Up')
plt.title('Speed Comparison between myDFT and np.fft.fft')
plt.grid(True)
plt.show()

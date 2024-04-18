import sounddevice as sd
from scipy.io import wavfile
import matplotlib.pyplot as plt

fileName = 'Klingon Windows start.wav'
fs, x = wavfile.read(fileName)

plt.close('all')
plt.plot(x)
sd.play(x, fs)
print('ok')
plt.show()


from scipy.io import wavfile
import myDSP
import matplotlib.pyplot as plt

fileName = r'C:\Windows\Media\ding.wav'
fs, x = wavfile.read(fileName)

plt.close('all')
myDSP.play(x, fs)
myDSP.plotInTime(x, fs)
plt.show()


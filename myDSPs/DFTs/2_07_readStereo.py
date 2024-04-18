import myDSP
import matplotlib.pyplot as plt

fileName = r'C:\Windows\Media\ding.wav'
fs, x = myDSP.readWav(fileName)

plt.close('all')
myDSP.play(x, fs)
myDSP.plotInTime(x, fs)
myDSP.plotInFrequency(x, fs)

x = x[:, 0]

myDSP.plotInTime(x, fs)
myDSP.plotInFrequency(x, fs)

plt.show()

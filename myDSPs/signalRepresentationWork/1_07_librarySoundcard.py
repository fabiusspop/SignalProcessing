import myDSP
import soundcard as sc
import time

mike = sc.default_microphone()
fs = 8000
t = 2
samples = fs * t

x = mike.record(samples, fs)

myDSP.play(x, fs)
myDSP.plotInTime(x[:, 0], fs)
myDSP.plotInTime(x[:, 1], fs)
time.sleep(2)
myDSP.play(x, 2 * fs)


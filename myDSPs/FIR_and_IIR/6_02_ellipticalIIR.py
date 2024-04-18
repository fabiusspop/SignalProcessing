# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.signal as sp
# import myDSP  # Assuming myDSP has appropriate functions for reading WAV and plotting
#
# fs, x = myDSP.readWav('Ring05c.wav')
#
# plt.close('all')
# plt.figure(figsize=[12, 12])
#
# plt.subplot(3, 2, 1)
# myDSP.plotInTime(x, fs)
# plt.title('Original Signal')
#
# plt.subplot(3, 2, 2)
# myDSP.plotInFrequency(x, fs)
# plt.title('Spectrum for the Original Signal')
#
# myDSP.play(x, fs)
#
# fc = 2000  # Cut-off frequency
# ft = 200   # Transition width
# wp = (fc - ft / 2) / (fs / 2)  # Passband edge normalized
# ws = (fc + ft / 2) / (fs / 2)  # Stopband edge normalized
# rp = 0.1  # Passband ripple in dB
# rs = 50   # Stopband attenuation in dB
#
# N, Wn = sp.ellipord(wp, ws, rp, rs)
# b, a = sp.ellip(N, rp, rs, Wn)
#
# f, H = sp.freqz(b, a, worN=256, fs=fs)
#
# plt.subplot(3, 2, 3)
# plt.plot(b, '.-b', label='b coefficients')
# plt.plot(a, '.-r', label='a coefficients')
# plt.legend()
# plt.title('Filter Coefficients')
#
# plt.subplot(3, 2, 4)
# plt.plot(f, abs(H), linewidth=3, label='Real frequency response')
# plt.plot([0, fc - ft/2, fc + ft/2, fs/2], [1, 1, 0, 0], 'k', label='Ideal frequency response')
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Gain')
# plt.grid(True)
# plt.legend()
#
# y = sp.lfilter(b, a, x, axis=0)
#
# plt.subplot(3, 2, 5)
# myDSP.plotInTime(y, fs)
# plt.title('Filtered Signal')
#
# plt.subplot(3, 2, 6)
# myDSP.plotInFrequency(y, fs)
# plt.title('Spectrum of the Filtered Signal')
#
# y = y.astype('int16')
#
# time.sleep(5)
#
# myDSP.play(y, fs)
#
# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.signal as sp
# import myDSP  # Assuming this module has the necessary functions as described
#
# # Load audio file
# fs, x = myDSP.readWav('Ring05c.wav')
#
# # Close all open figures
# plt.close('all')
#
# # Original signal in time domain
# myDSP.plotInTime(x, fs)
# plt.title('Original Signal')
# plt.show()
#
# myDSP.plotInFrequency(x, fs)
# plt.title('Spectrum for the Original Signal')
# plt.show()
#
# myDSP.play(x, fs)
#
# fc1 = 1000  # Cutoff frequency
# wCut = fc1 / (fs / 2)
# N = 101  # Filter order
#
# b = sp.firwin(N, wCut)
# a = [1.]  # FIR filter, so 'a' is just 1
#
# w, H = sp.freqz(b, a, worN=512)
# f = (w / np.pi) * (fs / 2)
#
# myDSP.freqResp(f, H)
# plt.title('Frequency Response')
# plt.show()
#
# y = sp.lfilter(b, a, x, axis=0)
#
# y = y * (x.max() / y.max())
# y = y.astype('int16')
#
# myDSP.plotInTime(y, fs)
# plt.title('Filtered Signal')
# plt.show()
#
# myDSP.plotInFrequency(y, fs)
# plt.title('Spectrum of the Filtered Signal')
# plt.show()
#
# myDSP.play(y, fs)

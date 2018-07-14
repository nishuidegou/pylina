# import the pyplot and wavfile modules

import matplotlib.pyplot as plot
from scipy.io import wavfile
import os
import numpy as np
from scipy import signal

# Read the wav file (mono)

# samplingFrequency, signalData = wavfile.read('./wav/output3.wav')
samplingFrequency, signalData = wavfile.read('./wav/output3-m.wav')
print(samplingFrequency,signalData.shape)
# print(signalData[:,0])
# np.savetxt('output2.txt',signalData[:,0],fmt='%d')
signalData = signalData[:,0]
# Plot the signal read from wav file
start_sample_point = 0
samples = 31744


plot.title('speech command test')

plot.subplot(311)
plot.plot(signalData[start_sample_point:start_sample_point+samples])
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(312)
# print(type(signalData[:,0]))
# plot.specgram(signalData[:,0], Fs=samplingFrequency)
plot.specgram(signalData[start_sample_point:start_sample_point+samples], Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')

plot.subplot(313)
f, t, Zxx = signal.stft(signalData, fs=samplingFrequency)
plot.pcolormesh(t, f, np.abs(Zxx))

plot.show()
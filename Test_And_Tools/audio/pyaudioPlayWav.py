"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys
import numpy as np
import matplotlib.pyplot as plot

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 22050#44100
RECORD_SECONDS = 2

# if len(sys.argv) < 2:
#     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#     sys.exit(-1)

# wf = wave.open(sys.argv[1], 'rb')
wf = wave.open('./wav/nihao.wav', 'rb')
# wf = wave.open('./wav/output3.wav', 'rb')

p = pyaudio.PyAudio()
print('sample width',wf.getsampwidth())
print('format',p.get_format_from_width(wf.getsampwidth()))
print('channel',wf.getnchannels())
print('sample rate',wf.getframerate())

stream = p.open(format=pyaudio.paInt16, #p.get_format_from_width(wf.getsampwidth()),
                channels=1,#wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# data = wf.readframes(CHUNK)
# while data != '':
#
#     stream.write(data)
#     data = wf.readframes(CHUNK)
#     # print(np.fromstring(data,'uint8'))
#     # allwave.append(np.fromstring(data,'uint8'))
#
# stream.stop_stream()
# stream.close()


# Plot the signal read from wav file
allwave = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = wf.readframes(CHUNK)
    # print(np.fromstring(data, 'int16'))
    allwave.append(np.fromstring(data, 'uint8'))

print(type(allwave))
plot.subplot(211)
plot.title('Spectrogram of a wav file with piano music')
plot.plot(allwave)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(212)
plot.specgram(np.array(allwave), Fs=RATE)
plot.xlabel('Time')
plot.ylabel('Frequency')

plot.show()

p.terminate()
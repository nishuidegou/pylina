import pyaudio
import numpy as np
import stft
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import time
from scipy.ndimage import uniform_filter1d

CHUNK = 4096*4#131264   #1024
WIDTH = 2
CHANNELS = 1#2
RATE = 44100#22050  #44100
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,           #format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNK)


print("* recording")
plt.ion()

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
while True:

    plt.clf()

    data = stream.read(CHUNK)
    print('source audio',type(data),data)
    # stream.write(data, CHUNK)
    # format_data = np.fromstring(data,'int8')
    format_data = np.fromstring(data, np.int16)
    # stream.write(np.int16(format_data), CHUNK)
    print('format data',type(format_data),format_data.shape,format_data)

    filtered_data = uniform_filter1d(format_data,size=32)
    """
    """
    # specgram = stft.spectrogram(format_data)
    # print('spectrogram',specgram)
    # print('spectogram imag',specgram.imag)
    # print(type(specgram.imag),specgram.shape)

    """
    plot data
    """

    plt.subplot(211)
    plt.plot(filtered_data)

    plt.subplot(212)
    plt.specgram(filtered_data,Fs=RATE)

    plt.pause(0.05)

    """
    processing spectrogram data here
    """
    # output = stft.ispectrogram(specgram)
    # print('output audio',np.int8(output))
    # print(type(output),output.shape)
    # stream.write(np.int16(format_data), CHUNK)

print("* done")

stream.stop_stream()
stream.close()

p.terminate()


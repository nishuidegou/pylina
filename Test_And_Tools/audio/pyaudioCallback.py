"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
This is the callback (non-blocking) version.
"""

import pyaudio
import time
import numpy

WIDTH = 2
CHANNELS = 2
RATE = 44100
CHUNK = 1024

p = pyaudio.PyAudio()

numpy.set_printoptions(threshold=2048)

def callback(in_data, frame_count, time_info, status):
    format_data = numpy.fromstring(in_data,'int16')
    print(format_data.size)

    # print(len(format_data))
    # print(format_data)
    #time.sleep(5)
    #--call pytorch to process the data
    #return (in_data, pyaudio.paContinue)
    return (in_data,pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    #time.sleep(0.1)
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()
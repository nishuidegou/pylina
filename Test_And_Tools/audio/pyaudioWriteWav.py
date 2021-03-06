"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1#2
RATE = 16000  #44100
RECORD_SECONDS = 2#5
WAVE_OUTPUT_FILENAME = "./wav/output3.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording",int(RATE / CHUNK * RECORD_SECONDS))

stream.stop_stream()
stream.close()
p.terminate()
print(frames)

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setsampwidth(1)
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
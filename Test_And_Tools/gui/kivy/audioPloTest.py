"""Real time plotting of Microphone level using kivy
"""

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import Graph, MeshLinePlot
from matplotlib import pyplot as plt

from kivy.clock import Clock
from threading import Thread
import audioop
import pyaudio
import numpy as np


def get_microphone_level():
    """
    source: http://stackoverflow.com/questions/26478315/getting-volume-levels-from-pyaudio-for-use-in-arduino
    audioop.max alternative to audioop.rms
    """
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()

    s = p.open(format=FORMAT,
               channels=CHANNELS,
               rate=RATE,
               input=True,
               frames_per_buffer=chunk)
    global levels

    while True:
        data = s.read(chunk)
        # print(type(data))
        mx = audioop.rms(data, 2)
        if len(levels) >= 100:
            levels = []
        levels.append(mx)
        # print(type(levels),levels)
        # print(type(np.array(levels)),np.array(levels))


class Logic(BoxLayout):
    def __init__(self,):
        super(Logic, self).__init__()
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        print(type(self.plot))
        self.spectrom = plt.specgram(np.array(levels), Fs=44100)


    def start(self):
        # self.ids.graph.add_plot(self.plot)
        # self.ids.graph.add_plot(self.spectrom)

        # Clock.schedule_interval(self.get_value, 0.001)
        Clock.schedule_interval(self.updata_spectrom, 0.01)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j/5) for i, j in enumerate(levels)]

    def updata_spectrom(self, dt):
        self.spectrom = plt.specgram(np.array(levels), Fs=44100)
        print(type(self.spectrom),self.spectrom)
        plt.show()


class RealTimeMicrophone(App):
    def build(self):
        return Builder.load_file("look.kv")
        # pass

if __name__ == "__main__":
    levels = []  # store levels of microphone
    get_level_thread = Thread(target = get_microphone_level)
    get_level_thread.daemon = True
    get_level_thread.start()
RealTimeMicrophone().run()
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import PNstreamsetup

a = PNstreamsetup.PNstreamsetup(rate=44100, updates=20)
a.stream_start()


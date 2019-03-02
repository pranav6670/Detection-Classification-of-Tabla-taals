import pyaudio
import time
import numpy as np
import threading

def getFFT(data,rate):
    """Given some data and rate, returns FFTfreq and FFT (half)."""
    data = data*np.hamming(len(data))
    fft = np.fft.fft(data)
    fft = np.abs(fft)
    freq = np.fft.fftfreq(len(fft), 1.0/rate)
    return freq[:int(len(freq)/2)], fft[:int(len(fft)/2)]


class PNHear:
    """
    The PNHear class is provides access to continuously recorded
    (and mathematically processed) microphone data.

    Arguments:

        device - the number of the sound card input to use. Leave blank
        to automatically detect one.

        rate - sample rate to use. Defaults to something supported.

        updatesPerSecond - how fast to record new data. Note that smaller
        numbers allow more data to be accessed and therefore high
        frequencies to be analyzed if using a FFT later
    """

    def __init__(self, device=None, rate=None, updatesPerSecond=10):
        self.p = pyaudio.PyAudio()
        self.chunk = 4096  # gets replaced automatically
        self.updatesPerSecond = updatesPerSecond
        self.chunksRead = 0
        self.device = device
        self.rate = rate

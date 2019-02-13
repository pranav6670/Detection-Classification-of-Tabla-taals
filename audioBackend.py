import numpy as np
import pyaudio
import time
import threading

def getFFT(data, rate):
    """Given some data and rate, returns FFTfreq and FFT (half)."""
    data = data*np.hamming(len(data))
    fft = np.fft.fft(data)
    fft = np.abs(fft)
    freq = np.fft.fftfreq(len(fft), 1.0/rate)
    return freq[:int(len(freq)/2)], fft[:int(len(fft)/2)]


class PNstream():



    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 4
        self.DEVICE = 2

        #############################################################
        print(self.p.get_device_count(), "device(s) detected.\n")
        for ii in range(self.p.get_device_count()):
            print(ii, self.p.get_device_info_by_index(ii)['name'])
        #############################################################

        # Open the stream
        #####################################
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
            input_device_index=self.DEVICE
        )
        ######################################








if __name__=="__main__":
    hear = PNstream(updatesPerSecond=10)  # Optionally set sample rate here
    while True:
        while lastRead == hear.chunksRead:
            time.sleep(.01)
        print(hear.chunksRead, len(hear.data))
        lastRead = hear.chunksRead
    print("DONE")


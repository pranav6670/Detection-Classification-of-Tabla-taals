import numpy as np
import pyaudio
import time
import threading
import sys
import struct

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
            input_device_index=0
        )
        ######################################

        ###########################################################
        # Check compatibility for params
        ###########################################################
        print("\nChecking compatibility with input parameters:" )
        print("\tAudio Device:", self.DEVICE)
        print("\tRate:", self.RATE)
        print("\tChannels:", self.CHANNELS)
        print("\tFormat:", self.FORMAT)

        isSupported = self.p.is_format_supported(input_format=self.FORMAT,
                                                 input_channels=self.CHANNELS,
                                                 rate=self.RATE,
                                                 input_device=self.DEVICE)
        if isSupported:
            print("\nThese settings are supported on device %i!\n" % self.DEVICE)
        else:
            sys.exit("\nOops-_-, these settings aren't",
                      " supported on device %i.\n" % self.DEVICE)
        #########################################################################

        while True:
            self.data = np.fromstring(self.stream.read(self.CHUNK, exception_on_overflow=False), dtype=np.int16)
            self.fftx, self.fft = getFFT(self.data, self.RATE)


if __name__=="__main__":
    PNstream()



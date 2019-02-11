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



    ### STREAM HANDLING

    def stream_readchunk(self):
        """reads some audio and re-launches itself"""
        try:
            self.data = np.fromstring(self.stream.read(self.chunk), dtype=np.int16)
            self.fftx , self.fft = getFFT(self.data, self.rate)

        except Exception as E:
            print(" -- exception! terminating...")
            print(E, "\n" * 5)
            self.keepRecording = False

        if self.keepRecording:
            self.stream_thread_new()
        else:
            self.stream.close()
            self.p.terminate()
            print(" -- stream STOPPED")

        self.chunksRead += 1

    def stream_thread_new(self):
        self.t = threading.Thread(target=self.stream_readchunk)
        self.t.start()

    def stream_start(self):
        """adds data to self.data until termination signal"""
        self.initiate()
        print(" -- starting stream")
        self.keepRecording = True  # set this to False later to terminate stream
        self.data = None  # will fill up with threaded recording data
        self.fft = None
        self.dataFiltered = None  # same
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1,
                                  rate=self.rate, input=True, frames_per_buffer=self.chunk)
        self.stream_thread_new()


if __name__=="__main__":
    hear = PNstream(updatesPerSecond=10)  # Optionally set sample rate here
    hear.stream_start()  # goes forever
    lastRead = hear.chunksRead
    while True:
        while lastRead == hear.chunksRead:
            time.sleep(.01)
        print(hear.chunksRead, len(hear.data))
        lastRead = hear.chunksRead
    print("DONE")


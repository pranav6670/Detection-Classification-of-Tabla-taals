import pyaudio
import numpy as np
import sys
import threading
import time

# Calculate FFT of input signal
def calculateFFT(data, rate):
    # Hamming window for FFT
    data = data * np.hamming(len(data))
    # abs for only magnitude(ignoring phase)
    fft = np.abs(np.fft.fft(data))
    # freq = 1/rate
    freq = np.fft.fftfreq(len(fft), 1.0 / rate)
    # Only positive frequency components
    return freq[:int(len(freq)/2)], fft[:int(len(fft)/2)]

class PNstreamsetup():
    """"
    This class provides access to continuously recorded
    data from the microphone.
    """
    def __init__(self, device=None, rate=None, updates=10):
        self.p = pyaudio.PyAudio()
        # Stream parameters
        self.chunk = 1024 * 4
        self.updates = updates
        self.device = device
        self.rate = rate

    def valid_low_rate(self, device):
        """
        Set the rate to the lowest supported audio rate.
        """
        for testrate in [44100]:
            if self.valid_test(device, testrate):
                return testrate
        print("SOMETHING'S WRONG! I can't figure out how to use DEV", device)
        return None

    def valid_test(self, device, rate=44100):
        """
        Given a device ID and a rate, return TRUE/False if it's valid.
        """
        try:
            self.info = self.p.get_device_info_by_index(device)
            if not self.info["maxInputChannels"] > 0:
                return False

            stream = self.p.open(
                format=pyaudio.paInt16,
                channels=1,
                input_device_index=device,
                frames_per_buffer=self.chunk,
                rate=int(self.info["defaultSampleRate"]),
                input=True)

            stream.close()

            return True

        except:
            return False

    def valid_input_devices(self):
        """
        See which devices can be opened for microphone input.
        call this when no PyAudio object is loaded.
        """
        mics = []
        for device in range(self.p.get_device_count()):
            if self.valid_test(device):
                mics.append(device)

        if len(mics) == 0:
            print("No microphone devices found!")
        else:
            print("Found %d microphone devices: %s" % (len(mics), mics))
        return mics

    def initiate(self):
        """
        Run this after changing settings (like rate) before recording
        """
        if self.device is None:
            self.device = self.valid_input_devices()[0] # Pick the first one

        if self.rate is None:
            self.rate = self.valid_low_rate(self.device)

        self.chunk = int(self.rate/self.updates) # Hold one tenth of a second in memory

        if not self.valid_test(self.device, self.rate):
            print("guessing a valid microphone device/rate...")
            self.device = self.valid_input_devices()[0] #pick the first one
            self.rate = self.valid_low_rate(self.device)

        self.datax = np.arange(self.chunk)/float(self.rate)
        msg = 'recording from "%s" ' % self.info["name"]
        msg += '(device %d) ' % self.device
        msg += 'at %d Hz' % self.rate
        print(msg)

    def close(self):
        """gently detach from things."""
        print(" -- sending stream termination command...")
        self.keepRecording = False #the threads should self-close

        while(self.t.isAlive()): #wait for all threads to close
            time.sleep(.1)

        self.stream.stop_stream()
        self.p.terminate()

    def stream_readchunk(self):
        """
        Reads some audio and re-launches itself
        """
        try:
            self.data = np.fromstring(self.stream.read(self.chunk), dtype=np.int16)
            self.fftx, self.fft = calculateFFT(self.data, self.rate)

        except Exception as E:
            print(" -- exception! terminating...")
            print(E, "\n"*5)
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
        """
        Adds data to self.data until termination signal
        """
        self.initiate()
        print(" -- starting stream")
        self.keepRecording = True # set this to False later to terminate stream
        self.data = None # will fill up with threaded recording data
        self.fft = None
        self.dataFiltered = None #same
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk)
        self.stream_thread_new()


if __name__ == "__main__":
    hear = PNstreamsetup(updates=10)  # optionally set sample rate here
    hear.stream_start()  # goes forever
    lastRead = hear.chunksRead
    while True:
        while lastRead == hear.chunksRead:
            time.sleep(.01)
        print(hear.chunksRead, len(hear.data))
        lastRead = hear.chunksRead
    print("DONE")
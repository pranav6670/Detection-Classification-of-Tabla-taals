import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import pyaudio
import sys
import struct
from scipy.fftpack import fft
import time

##########################
p = pyaudio.PyAudio()
##########################

######################################################
# Get number of devices
#######################################################
print(p.get_device_count(), "device(s) detected.\n")

for ii in range(p.get_device_count()):
    print(ii, p.get_device_info_by_index(ii)['name'])
#######################################################

##############################################
# Stream Parameters
###############################################
DEVICE = int(input("\nSelect device from above = "))# input returns 'str'
CHUNK = 1024*4
WINDOW = np.hamming(CHUNK)
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
###############################################

###########################################################
# Check compatibility for params
###########################################################
print("\nChecking compatibility with input parameters:")
print("\tAudio Device:", DEVICE)
print("\tRate:", RATE)
print("\tChannels:", CHANNELS)
print("\tFormat:", FORMAT)

isSupported = p.is_format_supported(input_format=FORMAT,
                                    input_channels=CHANNELS,
                                    rate=RATE,
                                    input_device=DEVICE)
if isSupported:
    print("\nThese settings are supported on device %i!\n" % DEVICE)
else:
    sys.exit("\nOops-_-, these settings aren't",
             " supported on device %i.\n" % DEVICE)
#########################################################################

#########################################
# Open the stream
#########################################
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                input_device_index=DEVICE
                )
##########################################

fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

x = np.arange(0, 2 * CHUNK, 2)       # samples (waveform)
xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)
####################################################################
# Create a line object with random data
line, = ax1.plot(x, np.random.rand(CHUNK), 'red', lw=0.5)
ax1.set_title('Raw audio')
ax1.set_xlabel('CHUNK')
ax1.set_ylabel('Amplitude')
# removing top and right borders
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
# adds major gridlines
ax1.grid(color='black', linestyle='-', linewidth=0.25, alpha=0.5)
ax1.set_ylim(0, 255)
ax1.set_xlim(0, CHUNK)
#####################################################################

#####################################################################
# Create semilogx line for spectrum
line_fft, = ax2.semilogx(xf, np.random.rand(CHUNK), '-', lw=2)
# Format spectrum axes
ax2.set_xlim(20, RATE / 2)
#####################################################################

while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 128
    line.set_ydata(data_int)
    # compute FFT and update line
    yf = fft(data_int)
    line_fft.set_ydata(np.abs(yf[0:CHUNK]) / (128 * CHUNK))
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()


import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import sys
import struct
import time

##########################
p = pyaudio.PyAudio()
##########################

######################################################
# Get number of devices
######################################################
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


fig, ax = plt.subplots()

x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(0, 255)
ax.set_xlim(0, CHUNK)

while True:
    data = stream.read(CHUNK)
    data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 128
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()




import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import sys

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
open = p.open(format=FORMAT,
              channels=CHANNELS,
              rate=RATE,
              input=True,
              frames_per_buffer=CHUNK,
              input_device_index=DEVICE
              )
##########################################





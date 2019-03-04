import pyaudio
import wave


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024 * 4
RECORD_SECONDS = 25
WAVE_OUTPUT_FILENAME = "test.wav"
# device_index = 2
audio = pyaudio.PyAudio()

print("----------------------record device list---------------------")
print(audio.get_device_count(), "device(s) detected.\n")
for devices in range(audio.get_device_count()):
    print(devices, audio.get_device_info_by_index(devices)['name'])
print("-------------------------------------------------------------")

index = int(input())
print("recording via index "+str(index))

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, input_device_index=index,
                    frames_per_buffer=CHUNK)
print("recording started")
Recordframes = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK, exception_on_overflow=False)
    Recordframes.append(data)
print("recording stopped")

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(Recordframes))
waveFile.close()

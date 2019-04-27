import librosa.display
import numpy as np
import matplotlib.pyplot as plt

y, sr = librosa.load('/home/pranav/Desktop/dataset/Trital/trital09.wav')

D = librosa.stft(y)
ref = np.max(np.abs(D))

librosa.display.specshow(librosa.amplitude_to_db(D, ref=ref), y_axis='log')
plt.colorbar()
plt.show()

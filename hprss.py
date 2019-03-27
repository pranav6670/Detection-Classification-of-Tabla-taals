from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
##########################################################
# Load the file
y, sr = librosa.load('/home/pranav/Desktop/myfinalProject/Test/'
                     'sample 4.wav')
##########################################################
# Compute the short-time Fourier transform of y
D = librosa.stft(y)
##########################################################
# Decompose the file
D_harmonic, D_percussive = librosa.decompose.hpss(D)
d_harmonic = librosa.istft(D_harmonic)
d_percussive = librosa.istft(D_percussive)
###################################################################################
# Write with margin = 1
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/har.wav', d_harmonic, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/per.wav', d_percussive, sr)
###################################################################################
rp = np.max(np.abs(D))

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(D, ref=rp), y_axis='log')
plt.colorbar()
plt.title('Full spectrogram')

plt.subplot(3, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(D_harmonic, ref=rp), y_axis='log')
plt.colorbar()
plt.title('Harmonic spectrogram')

plt.subplot(3, 1, 3)
librosa.display.specshow(librosa.amplitude_to_db(D_percussive, ref=rp), y_axis='log', x_axis='time')
plt.colorbar()
plt.title('Percussive spectrogram')
plt.tight_layout()
plt.savefig('1margin.png')
###############################################################################
D_harmonic2, D_percussive2 = librosa.decompose.hpss(D, margin=2)
D_harmonic4, D_percussive4 = librosa.decompose.hpss(D, margin=4)
D_harmonic6, D_percussive6 = librosa.decompose.hpss(D, margin=6)
D_harmonic8, D_percussive8 = librosa.decompose.hpss(D, margin=8)
D_harmonic10, D_percussive10 = librosa.decompose.hpss(D, margin=10)
###############################################################################
# Compute with margin > 2
d_harmonic2 = librosa.istft(D_harmonic2)
d_percussive2 = librosa.istft(D_percussive2)
d_harmonic4 = librosa.istft(D_harmonic4)
d_percussive4 = librosa.istft(D_percussive4)
d_harmonic6 = librosa.istft(D_harmonic6)
d_percussive6 = librosa.istft(D_percussive6)
d_harmonic8 = librosa.istft(D_harmonic8)
d_percussive8 = librosa.istft(D_percussive8)
d_harmonic10 = librosa.istft(D_harmonic10)
d_percussive10 = librosa.istft(D_percussive10)
#######################################################################################
# Write with margin > 2
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/har2.wav', d_harmonic2, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/per2.wav', d_percussive2, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/har4.wav', d_harmonic4, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/per4.wav', d_percussive4, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/har6.wav', d_harmonic6, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/per6.wav', d_percussive6, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/har8.wav', d_harmonic8, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/per8.wav', d_percussive8, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/har10.wav', d_harmonic10, sr)
librosa.output.write_wav('/home/pranav/Desktop/myfinalProject/per10.wav', d_percussive10, sr)
#######################################################################################
plt.figure(figsize=(10, 10))

plt.subplot(5, 2, 1)
librosa.display.specshow(librosa.amplitude_to_db(D_harmonic, ref=rp), y_axis='log')
plt.title('Harmonic')
plt.yticks([])
plt.ylabel('margin=1')

plt.subplot(5, 2, 2)
librosa.display.specshow(librosa.amplitude_to_db(D_percussive, ref=rp), y_axis='log')
plt.title('Percussive')
plt.yticks([]), plt.ylabel('')

plt.subplot(5, 2, 3)
librosa.display.specshow(librosa.amplitude_to_db(D_harmonic2, ref=rp), y_axis='log')
plt.yticks([])
plt.ylabel('margin=2')

plt.subplot(5, 2, 4)
librosa.display.specshow(librosa.amplitude_to_db(D_percussive2, ref=rp), y_axis='log')
plt.yticks([]), plt.ylabel('')

plt.subplot(5, 2, 5)
librosa.display.specshow(librosa.amplitude_to_db(D_harmonic4, ref=rp), y_axis='log')
plt.yticks([])
plt.ylabel('margin=4')

plt.subplot(5, 2, 6)
librosa.display.specshow(librosa.amplitude_to_db(D_percussive4, ref=rp), y_axis='log')
plt.yticks([]), plt.ylabel('')

plt.subplot(5, 2, 7)
librosa.display.specshow(librosa.amplitude_to_db(D_harmonic8, ref=rp), y_axis='log')
plt.yticks([])
plt.ylabel('margin=8')

plt.subplot(5, 2, 8)
librosa.display.specshow(librosa.amplitude_to_db(D_percussive8, ref=rp), y_axis='log')
plt.yticks([]), plt.ylabel('')

plt.subplot(5, 2, 9)
librosa.display.specshow(librosa.amplitude_to_db(D_harmonic10, ref=rp), y_axis='log')
plt.yticks([])
plt.ylabel('margin=10')

plt.subplot(5, 2, 10)
librosa.display.specshow(librosa.amplitude_to_db(D_percussive10, ref=rp), y_axis='log')
plt.yticks([]), plt.ylabel('')

plt.tight_layout()
plt.savefig('marginplots.png')
plt.show()
###################################################################################################


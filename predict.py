import os
import pickle
import numpy as np
from tqdm import tqdm
from scipy.io import wavfile
from python_speech_features import mfcc
from keras.models import load_model

def build_predictions(audio_dir):
    print('Extracting features from the data')

    for fn in tqdm(os.listdir(audio_dir)):
        rate, wav = wavfile.read(os.path.join(audio_dir, fn))

        for i in range(0, wav.shape[0]-config.step, config.step):
            sample = wav[i:i+config.step]

            x = mfcc(sample, rate, numcep=config.nfeat,
                     nfilt=config.nfilt, nfft=config.nfft)

            x = (x - config.min) / (config.max - config.min)

            if config.mode == 'conv':
                x = x.reshape(1, x.shape[0], x.shape[1], 1)
            elif config.mode == 'rec':
                x = np.expand_dims(x, axis=0)

            # if x.shape != (9 , 13 , 1): continue

            y_hat = model.predict(x)
            y_pred = np.argmax(y_hat)

    return y_pred

p_path = os.path.join('pickles', 'conv.p')

with open(p_path, 'rb') as handle:
    config = pickle.load(handle)

model = load_model(config.model_path)

y_preds = build_predictions('test')
print(y_preds)

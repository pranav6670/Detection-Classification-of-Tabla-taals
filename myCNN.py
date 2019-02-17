import keras
from keras.layers import Activation, Dense, Dropout, Flatten, \
    Conv2D, MaxPool2D
from keras.models import Sequential
import numpy as np
import librosa
import random


model = Sequential()

input_shape = (128, 128, 1)

model.add(Conv2D(24, (5, 5), strides=(1, 1), input_shape=input_shape))
model.add(MaxPool2D((4, 2), strides=(4, 2)))
model.add(Activation('relu'))

model.add(Conv2D(48, (5, 5), padding="valid"))
model.add(MaxPool2D((4, 2), strides=(4, 2)))
model.add(Activation('relu'))

model.add(Conv2D(48, (5, 5), padding="valid"))
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dropout(rate=0.5))

model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(rate=0.5))

model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(optimizer="Adam",
              loss="categorical_crossentropy",
              metrics=['accuracy']
              )


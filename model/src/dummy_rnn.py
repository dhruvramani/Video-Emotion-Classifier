import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM

timesteps, vector_dim, no_classes = 0, 0, 1

model = Sequential()
model.add(LSTM(128, input_shape=(timesteps, vector_dim))
model.add(Dropout(self.config.dropout))
model.add(Dense(no_classes, activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer=self.config.optimizer, metrics=['accuracy'])

x_train, y_train = get_data() # shape : [no_samples, timesteps, vector_dim], [no_samples, no_classes]
model.fit(x_train, y_train, batch_size=64, epochs=5)

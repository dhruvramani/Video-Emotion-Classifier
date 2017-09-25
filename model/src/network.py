import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM

class Network(object):
    def __init__(self, config):
        self.config = config
        self.max_features = 700
        self.model = self.create_model()

    def create_model(self):
        model = Sequential()
        model.add(Embedding(self.max_features, ouput_dim = 128))
        model.add(LSTM(128))
        model.add(Dropout(self.config.dropout))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer=self.config.optimizer, metrics=['accuracy'])
        return model

    def run_model(self, x_train, y_train):
        self.model.fit(x_train, y_train, batch_size=self.config.batch_size, epochs=self.config.max_epochs)

    def test(self, x_test, y_test):
        return model.evaluate(x_test, y_test, batch_size=self.config.batch_size)
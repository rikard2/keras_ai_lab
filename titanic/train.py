import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense
from keras.models import Sequential

from data import training_data, target_data

model = Sequential()
model.add(Dense(12, activation='relu', input_shape=(6,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
			   optimizer='adam',
			   metrics=['accuracy'])
model.fit(training_data, target_data, epochs=20, batch_size=1, verbose=1)

model.save("titanic.model")

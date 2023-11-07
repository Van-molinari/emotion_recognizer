from datetime import datetime
import numpy as np

from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential, load_model
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from keras.layers import (Conv1D, Dense, Dropout, Flatten, MaxPooling1D)
from sklearn.model_selection import train_test_split

class Model:
    def __init__(self):
        self.X_train = ""
        self.Y_train = ""
        self.X_test = ""
        self.Y_test = ""
        self.model = Sequential()
        self.filepath = 'model/speech_emotion_recognition.hdf5'

    def train(self, features, df):
        self.x = np.array(features['Feature'].tolist())
        self.y = np.array(df.Emotion.tolist())
        labelencoder = LabelEncoder()
        self.y = to_categorical(labelencoder.fit_transform(self.y))

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=1)
        self.X_train = self.X_train[:,:,np.newaxis]
        self.X_test = self.X_test[:,:,np.newaxis]
        num_labels = self.y.shape[1]

        self.model.add(Conv1D(128, kernel_size=(5), activation='relu', input_shape=(self.X_train.shape[1],1)))

        self.model.add(Conv1D(128, kernel_size=(5),activation='relu', padding='same'))
        self.model.add(MaxPooling1D(pool_size=(5)))

        self.model.add(Conv1D(256, kernel_size=(5),activation='relu', padding='same'))
        self.model.add(MaxPooling1D(pool_size=(5)))
        self.model.add(Dropout(0.2))

        self.model.add(Flatten())

        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(num_labels))

        self.model.add(Dense(units=4, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')

        num_epochs = 50
        num_batch_size = 64

        checkpointer = ModelCheckpoint(filepath=self.filepath,
                                    verbose=1, save_best_only=True)
        start = datetime.now()
        self.model.fit(self.X_train, self.Y_train, batch_size=num_batch_size, epochs=num_epochs,
                                validation_data=(self.X_test, self.Y_test), callbacks=[checkpointer], verbose=1)
        duration = datetime.now() - start
        print("[INFO] Treinamento concluído em:", duration)
        print(f"[INFO] Avaliação do modelo: {self.test()}%")

    def test(self):
        return self.model.evaluate(self.X_test, self.Y_test, verbose=0)[1]*100
    
    def call_model(self, input):
        return load_model(input)
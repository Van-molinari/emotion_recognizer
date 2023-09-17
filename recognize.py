import librosa
import numpy as np
from model import train_model

from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

# Insert new data
def predictSound(AUDIO, info = False, plot_waveform = False, plot_spectrogram = False):

    labelencoder = LabelEncoder()
    emotions_list = ['neutral', 'calm', 'happy', 'sad', 'angry', 'fear', 'disgust', 'surprise']
    y = ""
    y = to_categorical(labelencoder.fit_transform(np.array(emotions_list)))

    audio, sample_rate = librosa.load(AUDIO, sr = None, res_type='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=120)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    mfccs_scaled_features = mfccs_scaled_features.reshape(1,-1)
    mfccs_scaled_features = mfccs_scaled_features[:,:,np.newaxis]
    model = train_model.Model()
    model = model.call_model('model/speech_emotion_recognition.hdf5')

    predictions = model.predict(mfccs_scaled_features)
    print(predictions)
    predictions = predictions.argmax(axis=1)
    predictions = predictions.astype(int).flatten()
    predictions = (labelencoder.inverse_transform((predictions)))
    print('Resultado:', predictions)

predictSound('<enter_path_here>')
import librosa
import numpy as np
import speech_recognition as sr

from model import train_model
from pydub import AudioSegment
import os

from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

def convertAudio(audioFile):
    print(audioFile)
    if audioFile.endswith("mp3"): 
        audio = AudioSegment.from_mp3(audioFile)
        os.remove(audioFile)
        audio.export(audioFile.replace(".mp3", ".wav"), format="wav")

    elif audioFile.endswith("wav"):
        audio = AudioSegment.from_wav(audioFile)
        os.remove(audioFile)
        audio.export(audioFile, format="wav")
        
# Insert new data
def predictSound(AUDIO, info = False, plot_waveform = False, plot_spectrogram = False):

    labelencoder = LabelEncoder()
    emotions_list = ['neutral', 'happy', 'sad', 'angry']
    to_categorical(labelencoder.fit_transform(np.array(emotions_list)))

    audio, sample_rate = librosa.load(AUDIO, sr = None, res_type='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=120)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    mfccs_scaled_features = mfccs_scaled_features.reshape(1,-1)
    mfccs_scaled_features = mfccs_scaled_features[:,:,np.newaxis]
    model = train_model.Model()
    model = model.call_model('model/speech_emotion_recognition.hdf5')

    predictions = model.predict(mfccs_scaled_features)
    print(predictions)
    percentage = predictions[0][np.argmax(predictions)] * 100
    predictions = predictions.argmax(axis=1) # Média dos valores retornados
    predictions = (labelencoder.inverse_transform((predictions)))
    print('Resultado:', predictions, round(percentage, 2))
    return predictions[0], round(percentage, 2)

def returnText(audio):
    speech = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = speech.record(source)
    recognized_text = speech.recognize_google(audio_data)
    print(recognized_text)
    return recognized_text

# predictSound('<enter_path_here>')

# returnText("media/1001_IEO_DIS_HI.wav")
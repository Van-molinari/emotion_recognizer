import librosa
import numpy as np
import pandas as pd
import os
import sys

from tqdm import tqdm

class Dataset:
    def __init__(self, data_path):
        self.data_path = data_path
        self.extracted_features = []
        self.emotion_dict = {1: 'neutral', 2: 'happy', 3: 'sad', 4: 'angry'}

    def get_dataset(self):
        emotions = []
        full_path = []
        for path in self.data_path:
            for root, directory, files in os.walk(path):
                for file in files:
                    try:
                        if root.__contains__('RAVDESS'):
                            emotion = int(file[7:8])
                            if emotion == 2: emotion = 1
                            if emotion == 3: emotion = 2
                            if emotion == 4: emotion = 3
                            if emotion == 5: emotion = 4
                            if emotion == 6: emotion = 3
                            if emotion == 7: emotion = 3
                            if emotion == 8: emotion = 2
                            emotions.append(emotion)
                            full_path.append((root, file))

                        elif root.__contains__('CREMAD'):
                            emotion = str(file[9:12])
                            if emotion == 'NEU': emotion = 1
                            elif emotion == 'HAP': emotion = 2
                            elif emotion == 'SAD': emotion = 3
                            elif emotion == 'ANG': emotion = 4
                            elif emotion == 'FEA': emotion = 3
                            elif emotion == 'DIS': emotion = 3

                            emotions.append(emotion)
                            full_path.append((root, file))
                        
                        elif root.__contains__('TESS'):
                            if file.__contains__(".DS_Store"): pass
                            else:
                                emotion = str(file.split('_')[2][0:3])
                                if emotion.upper() == 'NEU': emotion = 1
                                elif emotion.upper() == 'HAP': emotion = 2
                                elif emotion.upper() == 'SAD': emotion = 3
                                elif emotion.upper() == 'ANG': emotion = 4
                                elif emotion.upper() == 'FEA': emotion = 3
                                elif emotion.upper() == 'DIS': emotion = 3
                                elif emotion.upper() == 'PS.': emotion = 2

                                emotions.append(emotion)
                                full_path.append((root, file))
                        
                    except ValueError:
                        continue

                    except Exception as e:
                        print(e)
                        sys.exit(1)
            
        return emotions, full_path
    
    def create_dataset(self, dataset):
        df = pd.DataFrame(dataset).T
        df.columns = ['Emotion', 'Path']
        df['Emotion'] = df['Emotion'].map(self.emotion_dict)
        df['Path'] = df['Path'].apply(lambda x: x[0] + '/' + x[1])

        return df
    
    def features_extractor(self, filename, n_mfcc):
        data, sample_rate = librosa.load(filename, sr = None, res_type = 'kaiser_fast')
        mfccs_features = librosa.feature.mfcc(y = data, sr = sample_rate, n_mfcc = n_mfcc)
        mfccs_scaled_features = np.mean(mfccs_features.T, axis = 0)

        return mfccs_scaled_features
    
    def create_features_dataset(self, files, n_mfcc):
        for path in tqdm(files):
            data = self.features_extractor(path, n_mfcc)
            self.extracted_features.append([data])

        df_features = pd.DataFrame(self.extracted_features, columns = ['Feature'])

        return df_features
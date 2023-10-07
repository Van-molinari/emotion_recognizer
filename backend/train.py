from dataset import dataset
from model import train_model

# Inicializa criação dos datasets
data = dataset.Dataset(['media/RAVDESS/Audio_Song_Actors_01-24', 'media/RAVDESS/Audio_Speech_Actors_01-24', 'media/CREMAD/AudioWAV'])
get_dataset = data.get_dataset() # Retorna dataset inicial dos áudios

df = data.create_dataset(get_dataset) # Retorna dataset formatado: emoção x áudio 
df_features = data.create_features_dataset(df.Path.values, 120) # Retorna features de cada áudio do dataset anterior

# Treinar o modelo
training = train_model.Model()
training.train(df_features, df)
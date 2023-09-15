import os

class Dataset:
    def __init__(self, data_path):
        self.data_path = data_path

    def create_dataset(self):
        modalitys = [] # Modalidade (01 = AV completo, 02 = apenas vídeo, 03 = apenas áudio).
        voc_channels = [] # Canal vocal (01 = fala, 02 = música).
        emotions = [] # Emoção (01 = neutro, 02 = calma, 03 = feliz, 04 = triste, 05 = zangado, 06 = com medo, 07 = nojo, 08 = surpreso).
        intensitys = [] # Intensidade emocional (01 = normal, 02 = forte). NOTA: Não há intensidade forte para a emoção 'neutra'.
        phrases =[] # Frase (01 = "Crianças conversam perto da porta", 02 = "Cachorros estão sentados na porta").
        actors = [] # Ator (01 a 24. Os atores com números ímpares são homens, os atores com números pares são mulheres)
        full_path = []
        for path in self.data_path:
            for root, directory, files in os.walk(path):
                for file in files:
                    try:
                        modal = int(file[1:2])
                        vchan = int(file[4:5])
                        label = int(file[7:8])
                        ints = int(file[10:11])
                        phr = int(file[13:14])
                        act = int(file[19:20])

                        modalitys.append(modal)
                        voc_channels.append(vchan)
                        emotions.append(label)
                        intensitys.append(ints)
                        phrases.append(phr)
                        actors.append(act)

                        full_path.append((root, file))
                    except ValueError:
                        continue
            
        return modalitys, voc_channels, emotions, intensitys, phrases, actors, full_path
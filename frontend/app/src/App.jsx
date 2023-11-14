import { styled } from "styled-components"
import EstilosGlobais from "./componentes/EstilosGlobais"
import SpeechBubble from "./componentes/SpeechBubble"
import Computer from "./componentes/Computer"
import Button from "./componentes/Button"
import { useState } from "react"
import { api } from "./API/api.js"
import photos from './componentes/Computer/fotos.json'

const Bottom = styled.div`
  background-color: var(--cor-primaria);
  width: 100%;
  height: 100vh;
  position: absolute;
  display: flex;
  //justify-content: space-around;
  align-items: center;
  flex-direction: column;
  color: var(--cor-letra);
`

function App() {
  const [speakComputer, setSpeakComputer] = useState('Clique no botão para inserir o áudio');
  const [speakAudio, setSpeakAudio] = useState('');
  const emotionPortuguese = {
    "neutral": "neutra",
    "happy": "feliz",
    "sad": "triste",
    "angry": "raiva",
  }
  const analyzesEmotions = async (audio) => {
    updateBubble("Espere, verificando áudio ...", "Espere, verificando áudio ...")
    const response = await api.sendAudio(audio)
    if (response.error) {
      updateBubble("Aconteceu um problema com o áudio ", response.error)
      updatePhoto("error")
    } else {
      const emotion = await api.emotion(response.id)
      updateBubble(emotion.message, "A emoção indetificada foi " + emotionPortuguese[emotion.emotion])
      updatePhoto(emotion.emotion)
    }
  }

  const updateBubble = (audio, computer) => {
    setSpeakAudio(audio)
    setSpeakComputer(computer)
  }

  const [imagem, setImagem] = useState(photos[0].imagem)
  const updatePhoto = (emotion) => {
    const newPhoto = photos.filter((photo) => {
      return photo.tag === emotion;
    })

    setImagem(newPhoto[0].imagem)
  }

  return (
    <Bottom>
      <EstilosGlobais />
      <SpeechBubble speak={speakComputer} />
      <Computer imagem={imagem} />
      <Button analyzesEmotions={analyzesEmotions} />
      <SpeechBubble speak={speakAudio} diz={'O que foi dito:'} />
    </Bottom>
  )
}

export default App

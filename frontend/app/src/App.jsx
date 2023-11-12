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
  const [speakComputer, setSpeakComputer] = useState('insert the audio');
  const [speakAudio, setSpeakAudio] = useState('');

  const analyzesEmotions = async (audio) => {
    updateBubble("Wait ...", "Wait ...")
    const response = await api.sendAudio(audio)
    if (response.error) {
      updateBubble("Something happened with audio", response.error)
      updatePhoto("error")
    } else {
      const emotion = await api.emotion(response.id)
      updateBubble(emotion.message, "The emotion identified was " + emotion.emotion)
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
      <SpeechBubble speak={speakAudio} diz={'What was said:'} />
    </Bottom>
  )
}

export default App

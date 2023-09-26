import { styled } from "styled-components"
import EstilosGlobais from "./componentes/EstilosGlobais"
import SpeechBubble from "./componentes/SpeechBubble"
import Computer from "./componentes/Computer"
import Button from "./componentes/Button"
import { useState } from "react"
import api from "./API/api"

const Fundo = styled.div`
  background-color: var(--cor-primaria);
  width: 100%;
  min-height: 100vh;
  position: absolute;
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
  color: var(--cor-letra);
`

function App() {
  const [speakComputer, setSpeakComputer] = useState('O que é');
  const [speakAudio, setSpeakAudio] = useState('');

  const [audio, setAudio] = useState()
  async function enviaAudio() {
    api.enviaAudio(audio)
  }

  return (
    <Fundo>
      <EstilosGlobais/>
      <SpeechBubble speak={speakComputer}/>
      <Computer/>
      <Button setAudio={setAudio} enviaAudio={enviaAudio}/>
      <h3>O que foi dito:</h3>
      <SpeechBubble speak={speakAudio}/>
    </Fundo>
  )
}

export default App

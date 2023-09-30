import { styled } from "styled-components"
import EstilosGlobais from "./componentes/EstilosGlobais"
import SpeechBubble from "./componentes/SpeechBubble"
import Computer from "./componentes/Computer"
import Button from "./componentes/Button"
import { useState } from "react"
import { api } from "./API/api.js"

const Fundo = styled.div`
  background-color: var(--cor-primaria);
  width: 100%;
  min-height: 100vh;
  position: absolute;
  display: flex;
  //justify-content: space-around;
  align-items: center;
  flex-direction: column;
  color: var(--cor-letra);
`

function App() {
  const [speakComputer, setSpeakComputer] = useState('O que é');
  const [speakAudio, setSpeakAudio] = useState('');

  const analisaEmocoes = async (audio) => {
    setSpeakAudio("Aguarde ...")
    setSpeakComputer("Aguarde ...")
    const retorno = await api.enviaAudio(audio)
    const emocao = await api.emocao(retorno.id)
    setSpeakAudio(emocao.message)
    setSpeakComputer(emocao.emotion)
  }

  return (
    <Fundo>
      <EstilosGlobais/>
      <SpeechBubble speak={speakComputer}/>
      <Computer/>
      <Button analisaEmocoes={analisaEmocoes}/>
      <SpeechBubble speak={speakAudio} diz={'O que foi dito:'}/>
    </Fundo>
  )
}

export default App

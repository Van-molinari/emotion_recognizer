import { styled } from "styled-components"
import EstilosGlobais from "./componentes/EstilosGlobais"
import SpeechBubble from "./componentes/SpeechBubble"
import Computer from "./componentes/Computer"
import Button from "./componentes/Button"
import { useState } from "react"

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
  const [speakComputer, setSpeakComputer] = useState('O que é um Hook? Um Hook é uma função especial que te permite utilizar recursos do React. Por exemplo, useState é um Hook que te permite adicionar o state do React a um componente de função. Vamos aprender outros Hooks mais tarde Quando eu deveria usar um Hook Se você escreve um componente de função e percebe que precisa adicionar algum state para ele, anteriormente você tinha que convertê-lo para uma classe. Agora você pode usar um Hook dentro de um componente de função existente. Vamos fazer isso agora mesmo');
  const [speakAudio, setSpeakAudio] = useState('Audio');

  const [audio, setAudio] = useState('')
  

  return (
    <Fundo>
      <EstilosGlobais/>
      <SpeechBubble speak={speakComputer}/>
      <Computer/>
      <Button setAudio={setAudio}/>
      <h3>O que foi dito:</h3>
      <SpeechBubble speak={speakAudio}/>
    </Fundo>
  )
}

export default App

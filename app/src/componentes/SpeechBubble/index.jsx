import styled from "styled-components"

const Balloon = styled.textarea`
    width: 50vw;
    height: 10vh;
    background-color: var(--cor-secundaria);
    border: 1px solid var(--cor-borda);
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    resize: none;

    color: var(--cor-letra);
    
    &::-webkit-scrollbar{
      width: 3px;
    }
`

// eslint-disable-next-line react/prop-types
export default function SpeechBubble({speak}) {

  return (
    <Balloon readOnly value={speak}/>
  )
}

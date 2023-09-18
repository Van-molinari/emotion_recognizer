import styled from "styled-components"

const Balloon = styled.textarea`
    width: 50vw;
    height: 10vh;
    background-color: white;
    border: 1px solid black;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    resize: none;
    
    &::-webkit-scrollbar{
      width: 3px;
    }
`

export default function SpeechBubble({speak}) {

  return (
    <Balloon readOnly value={speak}/>
  )
}

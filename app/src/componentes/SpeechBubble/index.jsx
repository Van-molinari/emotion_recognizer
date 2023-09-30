import styled from "styled-components"

const Balloon = styled.textarea`
    width: 50vw;
    height: 10vh;
    background-color: var(--cor-secundaria);
    border: 1px solid var(--cor-borda);
    padding: 10px;
    margin: 20px;
    border-radius: 10px;
    text-align: center;
    resize: none;

    color: var(--cor-letra);
    
    &::-webkit-scrollbar{
      width: 3px;
    }
`
const H3styled = styled.h3`
  margin-bottom: 0;
  width: 50vw;
`

// eslint-disable-next-line react/prop-types
export default function SpeechBubble({speak, diz}) {

  return (
    <>
      <H3styled>{diz}</H3styled>
      <Balloon readOnly value={speak} />
    </>
  )
}

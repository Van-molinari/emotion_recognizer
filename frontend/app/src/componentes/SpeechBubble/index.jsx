import styled from "styled-components"

const Balloon = styled.textarea`
    width: 50vw;
    height: 10vh;
    min-height: 3vh;
    background-color: var(--cor-secundaria);
    border: 1px solid var(--cor-borda);
    padding: 10px;
    margin-bottom: 3vh;
    border-radius: 10px;
    text-align: center;
    font-family: var(--fonte);
    font-size: 1.7rem;
    resize: none;

    color: var(--cor-letra);
    
    &::-webkit-scrollbar{
      width: 3px;
    }
`
const H3styled = styled.h3`
  margin-bottom: 1px;
  font-family: var(--fonte);
  width: 50vw;
  font-size: 1.3rem;
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

import styled from 'styled-components'
 


const Image = styled.img`
  
  width: 100%;
  height: 100%;
  
`
const Painel = styled.div`
  margin-top: 5vh;
  max-width: 45vh;
  max-height: 45vh;
  width: 40vw

`

export default function Computer({imagem}) {

  return (
    <Painel>
        <Image src={imagem} 
        alt="image of a compure smiling" />
    </Painel>
  )
}

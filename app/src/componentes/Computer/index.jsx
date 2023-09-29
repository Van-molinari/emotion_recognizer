import styled from 'styled-components'
import computerSmiling from './compureSmiling.png'  

const Image = styled.img`
  margin-top: 35px;
`

export default function Computer() {
  return (
    <div>
        <Image src={computerSmiling} alt="image of a compure smiling" />
    </div>
  )
}

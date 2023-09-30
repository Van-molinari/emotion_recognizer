import styled from "styled-components"

const File = styled.input`
    display:none;
`

const Label = styled.label`
    width: 10vw;
    height: 3vh;
    background-color: var(--cor-secundaria);
    border: 1px solid var(--cor-borda);
    color: var(--cor-letra);
    padding: 10px;
    border-radius: 15px;
    text-align: center;

    &:hover{
        width: 12vw;
        height: 5vh; 
    }
`

const DivStyle = styled.div`
    margin-top: 13vh;
    margin-bottom: 20px;
`

// eslint-disable-next-line react/prop-types
export default function Button({ analisaEmocoes }) {
    return (
        <DivStyle>
            <Label htmlFor="audio"> Escolher áudio</Label>
            <File className="audio"
                id="audio"
                type="file"
                accept="audio/*"
                onChange={(event) => {
                    analisaEmocoes(event.target.files[0])                 
                }}
            />
        </DivStyle>
    )
}

import styled from "styled-components"
import enviaAudio from "../../API/api"

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
`

// eslint-disable-next-line react/prop-types
export default function Button({ setAudio }) {
    return (
        <div>
            <Label htmlFor="audio"> Escolher áudio</Label>
            <File className="audio"
                id="audio"
                type="file"
                accept="audio/*"
                onChange={(event) => {
                    setAudio(event.target.files[0])
                    enviaAudio()                 
                }}
            />
        </div>
    )
}

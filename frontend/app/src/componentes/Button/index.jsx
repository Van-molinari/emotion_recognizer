import styled from "styled-components"

const File = styled.input`
    display:none;
`

const Label = styled.label`
    display: flex;
    justify-content: center;
    align-items: center;
    width: 15vw;
    height: 6vh;
    min-width: 80px;
    background-color: var(--cor-secundaria);
    border: 1px solid var(--cor-borda);
    color: var(--cor-letra);
    padding: 10px;
    border-radius: 15px;
    text-align: center;
    font-size: 1rem;
    cursor:pointer;

    &:hover{
        transform: scale(1.1);
        background-color: var(--cor-primaria);
    }
`

const DivStyle = styled.div`
    margin-top: 5vh;
    margin-bottom: 5vh;
    
`

// eslint-disable-next-line react/prop-types
export default function Button({ analyzesEmotions }) {
    return (
        <DivStyle>
            <Label htmlFor="audio"> CHOOSE AUDIO</Label>
            <File className="audio"
                id="audio"
                type="file"
                accept="audio/*"
                onChange={(event) => {
                    analyzesEmotions(event.target.files[0])
                }}
            />
        </DivStyle>
    )
}

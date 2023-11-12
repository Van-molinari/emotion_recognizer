async function sendAudio(audio) {
    const formData = new FormData();
    formData.append('file', audio);
    const connection = await fetch("http://localhost:5500/data/upload", {
        method: "POST",
        body: formData,
    })
    if (connection.status == 400) {
        const erroJson = await connection.json();
        return erroJson
    }
    const connectionConverted = await connection.json();
    return connectionConverted
}

async function emotion(id) {
    try {
        const connection = await fetch(`http://localhost:5500/search/${id}`)
        const connectionEmotionConverted = await connection.json()
        if (connectionEmotionConverted.erro) {
            throw Error('ID does not exist')
        }
        return connectionEmotionConverted
    } catch (erro) {
        console.log(erro);
    }
}

export const api ={ 
    sendAudio,
    emotion
}
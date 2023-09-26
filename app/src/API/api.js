async function enviaAudio(audio) {
    const formData = new FormData();
    formData.append('file', audio);
    const conexao =await fetch("http://localhost:5500/recognize/", {
        method:"POST",
        headers: {
            "Content-type": "multipart/form-data",
            "Access-Control-Allow-Origin": "http://localhost:5173/",
            "file": formData

        },
    })
    if (!conexao.ok) {
        throw new Error("Não foi possível enviar audio")
    }
    const conexaoConvertida = await conexao.json();
    console.log(conexaoConvertida);
    return conexaoConvertida
}

export default enviaAudio;
async function enviaAudio(audio) {
    console.log(audio);
    const formData = new FormData();
    formData.append('file', audio);
    const conexao =await fetch("http://localhost:5500/data/upload", {
        method:"POST",
        /* headers: {
            "Content-type": "multipart/form-data",
            "file": formData
        }, */
        body: formData,
    })
    if (!conexao.ok) {
        throw new Error("Não foi possível enviar audio")
    }
    const conexaoConvertida = await conexao.json();
    console.log(conexaoConvertida);
    return conexaoConvertida
}

export default enviaAudio;
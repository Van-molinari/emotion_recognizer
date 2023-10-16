async function enviaAudio(audio) {
    const formData = new FormData();
    formData.append('file', audio);
    const conexao = await fetch("http://localhost:5500/data/upload", {
        method: "POST",
        body: formData,
    })
    if (!conexao.ok) {
        throw new Error("Não foi possível enviar audio")
    }
    const conexaoConvertida = await conexao.json();
    return conexaoConvertida
}

async function emocao(id) {
    try {
        const conexao = await fetch(`http://localhost:5500/recognize/${id}`)
        const conexaoEmocaoConvertida = await conexao.json()
        if (conexaoEmocaoConvertida.erro) {
            throw Error('ID nao existe')
        }
        return conexaoEmocaoConvertida
    } catch (erro) {
        console.log(erro);
    }
}

export const api ={ 
    enviaAudio,
    emocao
}
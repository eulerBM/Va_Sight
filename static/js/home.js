function copiarTexto(botao) {
    // Encontra o elemento 'key_copy' dentro do card específico
    var campo = botao.parentElement.querySelector("#key_copy");

    if (campo) {
        var range = document.createRange();
        range.selectNode(campo);

        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);

        try {
            document.execCommand('copy');
            alert("Texto copiado: " + campo.textContent);
        } catch (err) {
            console.error('Erro ao tentar copiar texto:', err);
            alert('Erro ao tentar copiar texto. Consulte o console para mais detalhes.');
        } finally {
            window.getSelection().removeAllRanges();
        }
    } else {
        console.error('Elemento com ID "key_copy" não encontrado dentro do card.');
    }
}

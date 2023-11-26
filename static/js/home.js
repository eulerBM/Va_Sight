
function copiarTexto() {
    // Seleciona o elemento de texto
    var campo = document.getElementById("key_copy");

    // Cria um intervalo para selecionar o conteúdo do elemento
    var range = document.createRange();
    range.selectNode(campo);

    // Remove qualquer seleção anterior
    window.getSelection().removeAllRanges();

    // Adiciona o novo intervalo ao seletor
    window.getSelection().addRange(range);

    // Executa o comando de cópia
    document.execCommand('copy');

    // Deseleciona o campo
    window.getSelection().removeAllRanges();

    // Você pode adicionar feedback ao usuário, por exemplo, alerta ou mensagem
    alert("Texto copiado: " + campo.textContent);
}
document.addEventListener("DOMContentLoaded", () => {
    const aviso = document.getElementById("aviso-width");
    const aviso_close_button = document.querySelector("#aviso .close");

    try {
        aviso_close_button.addEventListener("click", () => {
            aviso.setAttribute('reverse', '');
        });
    } catch (e) {}

    const sucsess = document.getElementById("sucsess");
    const sucsess_close_button = document.querySelector("#sucsess .close");
    try {
        sucsess_close_button.addEventListener("click", () => {
            sucsess.setAttribute('reverse', '');
        });
    } catch (e) {}

    const error = document.getElementById("error");
    const error_close_button = document.querySelector("#error #error-content .close");

    try {
        error_close_button.addEventListener("click", () => {
            error.setAttribute('reverse', '');
        });
    } catch (e) {}

    const quebrar_linha = document.getElementById("quebrar-linha-demo");
    quebrar_linha.innerText = 'texto<br>';

    const subtema = document.getElementById("subtema-demo");
    subtema.innerText = '# texto';

    const negrito = document.getElementById("negrito");
    negrito.innerText = '**texto**';

    const italico = document.getElementById("italico");
    italico.innerText = '*texto*';

    const citacao = document.getElementById("citacao");
    citacao.innerText = '> texto';

    const link = document.getElementById("link");
    link.innerText = '[Texto aqui](https://Link-aqui)';

    const preview_button = document.getElementById("preview-button");
    const preview_content = document.querySelector(".preview-content .preview");
    preview_button.addEventListener("click", () => {
        document.querySelector(".preview-content").style.display = 'block';
        var converter = new showdown.Converter();
        var text = document.getElementById("text").value;
        var html = converter.makeHtml(text);
        preview_content.innerHTML = html;
    });
});
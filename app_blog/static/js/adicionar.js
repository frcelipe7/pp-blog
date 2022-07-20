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
});
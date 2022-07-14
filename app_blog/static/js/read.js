function click_button (button1, button2) {
    try {
        button1.removeAttribute("bye");
        button2.removeAttribute("bye");
    } catch(e) {}
    try {
        button1.removeAttribute("hi");
        button2.removeAttribute("hi");
    } catch(e) {}
    button1.setAttribute("bye", '');

    button1.addEventListener('animationend', () => {
        button1.style.display = 'none';
        button1.style.opacity = '0';

        button2.style.display = '';
        button2.setAttribute('hi', '');
    });
};

addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".block .info-buttons .buttons .save");
    const button_salvo = document.querySelector(".block .info-buttons .buttons .salvo");

    const info_buttons = document.querySelector(".block .text-content .info-buttons");
    const side_bar_left = document.querySelector(".sidebar-right");

    button.addEventListener("click", () => {
        click_button(button, button_salvo);
    }, {once: true});

    button_salvo.addEventListener("click", () => {
        click_button(button_salvo, button);
    }, {once: true});
});

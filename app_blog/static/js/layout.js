document.addEventListener("DOMContentLoaded", () => {
    const menu = document.querySelector(".menu_hamburger");
    const aside = document.querySelector("aside");

    menu.addEventListener("click", () => {
        if ('open-menu' in menu.attributes) {
            menu.removeAttribute('open-menu');
            menu.setAttribute('close-menu', '');
            aside.style.left = '-300px';
        } else {
            menu.removeAttribute('close-menu');
            menu.setAttribute('open-menu', '');
            aside.style.left = '0px';
        };
    });
});
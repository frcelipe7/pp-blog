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


    // search functions
    
    const search_button = document.querySelector(".content-buttons .search button");
    const search_input = document.querySelector(".content-buttons .search input");

    const site_domain = "http://127.0.0.1:8000";
    
    function search(search) {
        window.location.href = `${site_domain}/search?keyword_search=${search}`;
    };
    
    function enterKeyPressed(event, value) {
        if (event.keyCode == 13) {
            search(value);
            return true;
        } else {
            return false;
        }
    };
    
    search_button.addEventListener('click', () => {
        if (search_input.value == "") return false;

        search(search_input.value);
    });

    search_input.addEventListener("keypress", () => {
        if (search_input.value == "") return false;

        enterKeyPressed(event, search_input.value);
    });

    try {
        const second_search_input = document.querySelector(".search_form #second_search");
        const second_search_button = document.querySelector(".search_form button");

        second_search_button.addEventListener("click", () => {
            search(second_search_input.value);
        });

        second_search_input.addEventListener("keypress", () => {
            enterKeyPressed(event, second_search_input.value);
        });
    } catch (e) {};
});
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
    
    function search() {
        if (search_input.value != "") {
            const site_domain = "http://127.0.0.1:8000";
            window.location.href = `${site_domain}/search?keyword_search=${search_input.value}`;
        };
    };
    
    function enterKeyPressed(event) {
        if (event.keyCode == 13) {
            search();
            return true;
        } else {
            return false;
        }
    };
    
    search_button.addEventListener('click', () => {
        search();
    });

    search_input.addEventListener("keypress", () => {
        enterKeyPressed(event);
    });
});
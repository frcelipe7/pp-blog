function verify_if_saved(save_button, clicked) {
    if (clicked == true) {
        if (save_button.dataset.saved == 'false') {
            save_button.dataset.saved = 'true';
        } else {
            save_button.dataset.saved = 'false'
        }
        
    } 
        
    if (save_button.dataset.saved == 'false') {
        save_button.innerHTML = `
            <p>Salvar</p>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
                <!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com 
                    License - https://fontawesome.com/license (Commercial License) Copyright 
                    2022 Fonticons, Inc. 
                -->
                <path d="M336 0h-288C21.49 0 0 21.49 0 48v431.9c0 24.7 26.79 40.08 48.12 
                27.64L192 423.6l143.9 83.93C357.2 519.1 384 504.6 384 479.9V48C384 21.49 
                362.5 0 336 0zM336 452L192 368l-144 84V54C48 50.63 50.63 48 53.1 48h276C333.4 
                48 336 50.63 336 54V452z"/>
            </svg>
        `;
    } else {
        save_button.innerHTML = `
            <p>Salvo</p>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
                <!--! Font Awesome Pro 6.1.1 by @fontawesome -
                    https://fontawesome.com License - https://fontawesome.com/license 
                    (Commercial License) Copyright 2022 Fonticons, Inc. 
                -->
                <path d="M384 48V512l-192-112L0 512V48C0 21.5 21.5 0 48 0h288C362.5 
                0 384 21.5 384 48z"/>
            </svg> 
        `;
    };
};

addEventListener("DOMContentLoaded", () => {
    const save_button = document.querySelector(".block .info-buttons .buttons .save");

    const info_buttons = document.querySelector(".block .text-content .info-buttons");
    const side_bar_left = document.querySelector(".sidebar-right");

    verify_if_saved(save_button, clicked=false);

    save_button.addEventListener("click", () => {
        verify_if_saved(save_button, clicked=true);
    });
});

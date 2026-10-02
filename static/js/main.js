/*
    Global JavaScript.

    This controls interactions shared across the website,
    starting with the responsive navigation.
*/

const menuButton = document.querySelector(".mobile-menu-toggle");
const navigation = document.querySelector(".site-nav-links");


if (menuButton && navigation) {

    menuButton.addEventListener("click", () => {

        // Open or close the mobile navigation panel.
        navigation.classList.toggle("is-open");

        const isOpen = navigation.classList.contains("is-open");

        // Keep the accessibility state synchronized.
        menuButton.setAttribute("aria-expanded", isOpen);
    });
}
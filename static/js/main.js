/*
    Global JavaScript.

    This file controls interactions shared across the website:
    1. Responsive navigation
    2. Scroll-based reveal animations
*/


/* =========================================================
   MOBILE NAVIGATION
   ========================================================= */

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


/* =========================================================
   SCROLL REVEAL ANIMATIONS
   ========================================================= */

/*
    IntersectionObserver watches elements as they enter the
    visitor's screen.

    This means animations happen while scrolling instead of
    everything animating immediately when the page loads.
*/

const revealElements = document.querySelectorAll(".reveal");


if (revealElements.length) {

    const revealObserver = new IntersectionObserver(
        (entries, observer) => {

            entries.forEach((entry) => {

                // Only animate when the element becomes visible.
                if (entry.isIntersecting) {

                    entry.target.classList.add("is-visible");

                    // Stop watching after the animation has started.
                    observer.unobserve(entry.target);
                }
            });

        },
        {
            // Start the animation shortly before the element
            // completely enters the screen.
            threshold: 0.15
        }
    );


    revealElements.forEach((element) => {
        revealObserver.observe(element);
    });
}
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
    // Make sure image reveals are also triggered reliably.
    document.querySelectorAll(".reveal-image").forEach((element) => {
        if (element.getBoundingClientRect().top < window.innerHeight) {
            element.classList.add("is-visible");
        }
    });
}

/* =========================================================
   JOURNEYS MAP — SCROLL PARALLAX
   ========================================================= */

/*
    Gives the decorative Sikkim map a gentle parallax movement.

    The map moves independently from the content, creating
    depth while scrolling through the Journeys section.
*/

const journeysMap = document.querySelector(".journeys-map");
const journeysSection = document.querySelector(".journeys-section");

if (journeysMap && journeysSection) {

    let mapAnimationFrame = null;

    const updateJourneysMap = () => {

        const rect = journeysSection.getBoundingClientRect();

        /*
            Only animate while the Journeys section is visible.
        */
        if (
            rect.bottom > 0 &&
            rect.top < window.innerHeight
        ) {

            /*
                Calculate how far the section has travelled
                through the viewport.

                The 70px range makes the movement noticeable
                without making the map feel disconnected.
            */
            const progress =
                (window.innerHeight - rect.top) /
                (window.innerHeight + rect.height);

            const movement =
                (progress - 0.5) * 70;

            journeysMap.style.transform =
                `translate3d(0, ${movement}px, 0)`;
        }

        mapAnimationFrame = null;
    };


    window.addEventListener(
        "scroll",
        () => {

            /*
                Prevent excessive calculations while scrolling.
            */
            if (!mapAnimationFrame) {

                mapAnimationFrame =
                    requestAnimationFrame(updateJourneysMap);
            }

        },
        { passive: true }
    );


    /*
        Set the initial position immediately.
    */
    updateJourneysMap();
}
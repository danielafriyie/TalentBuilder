const navSlide = () => {
    const mobileLines = document.querySelector('.mobile-lines');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    // toggle nav
    mobileLines.addEventListener('click', () => {
        nav.classList.toggle('nav-active')
    });

    // animate links
    navLinks.forEach((link, index) => {
        // console.log(index)
    });
};

navSlide();
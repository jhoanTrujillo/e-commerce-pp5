// Provides code with own self-contain scope.
(() => {     
    const mobileNavbar = () => {
        const navbarBurger = document.getElementById('navbar-burger');
        const mobileNavbar = document.getElementById('mobile-navbar');
    
        navbarBurger.addEventListener('click', (event) => {
            const isActive = event.currentTarget.classList.contains('is-active');
            event.currentTarget.classList.toggle('is-active');
    
            if (isActive) {
                mobileNavbar.classList.remove('has-slide-animation-open');
                mobileNavbar.classList.add('has-slide-animation-close');
            } else {
                mobileNavbar.classList.remove('has-slide-animation-close');
                mobileNavbar.classList.add('has-slide-animation-open');
            }
        });
    };

    mobileNavbar();
})();
// // Provides code with its own self-contained scope.
// (() => {     
//     const mobileNavbar = () => {
//         const navbarBurger = document.getElementById('navbar-burger');
//         const mobileNavbar = document.getElementById('mobile-navbar');
        
//         navbarBurger.addEventListener('click', (event) => {
//             const isActive = event.currentTarget.classList.contains('is-active');
//             event.currentTarget.classList.toggle('is-active');
    
//             if (isActive) {
                
//                 mobileNavbar.classList.remove('has-slide-animation-open');
//                 mobileNavbar.classList.add('has-slide-animation-close');

//                 // Return body to default scroll behaviour
//                 disableBodyScrolling(isActive);
//             } else {
//                 // Prevents body from scrolling when navbar is open

//                 mobileNavbar.classList.remove('has-slide-animation-close');
//                 mobileNavbar.classList.add('has-slide-animation-open');
                
//                 // Prevent scrolling when navbar is open on mobile
//                 disableBodyScrolling(isActive);
//             }
//         });
//     }

//     const disableBodyScrolling = (isActive) => {
//         const body = document.querySelector('#body-container');

//         if (!isActive) {
//             // Disable body scrolling
//             body.classList.add('non-scrolling');
//         } else {
//             // Enable body scrolling
//             body.classList.remove('non-scrolling');
//         }
//     }

//     mobileNavbar();
// })();

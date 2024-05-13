class Message extends HTMLElement {
	constructor() {
	  super();
	}
  
	connectedCallback() {
	  // Add event listener to handle click on delete button
	  this.querySelector('button[aria-label="delete"]').addEventListener('click', this.deleteMessage.bind(this));
	  this.style.width = '20rem'
	}
  
	deleteMessage() {
	  // Remove the message element from the DOM
	  this.remove();
	}
  }

// Debounce form submittion to prevent multiple submittions
const setupFormSubmitListener = () => {
    const forms = document.querySelectorAll('form');

    forms.forEach(parentForm => {
        const submitButton = parentForm.querySelector('button[type="submit"]');
        const formInputs = parentForm.querySelectorAll('input, select, textarea');

        parentForm.addEventListener('submit', (event) => {
            event.preventDefault();

            // Add is-skeleton class to the submit button
            submitButton.classList.add('is-skeleton');

            // Add is-skeleton class to all inputs in the form
            formInputs.forEach(input => {
                input.classList.add('is-skeleton');
            });

            // Submit the form after a brief delay
            setTimeout(() => {
                parentForm.submit();
            }, 500);
        });
    });
};

// Navbar

function setupNavbarBurger() {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
        el.addEventListener('click', () => {
            // Get the target from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');
        });
    });
}

// Define class elements
window.customElements.define('message-box', Message);

// Call the functions when the DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
    setupNavbarBurger();
	setupFormSubmitListener();
});


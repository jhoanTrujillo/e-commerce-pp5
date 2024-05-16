(() => {
class MessageBox extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        // Add event listener to handle click on delete button
        this.querySelector('button[aria-label="delete"]').addEventListener('click', this.deleteMessage.bind(this));
        this.style.width = '20rem';

        // Schedule fade-out and deletion after one second
        setTimeout(() => {
            this.fadeOutAndDelete();
        }, 2000);
    }

    fadeOutAndDelete() {
        // Add 'fade-out' class to trigger fade-out animation
        this.classList.add('fade-out');

        // Listen for 'animationend' event to remove the element after animation completes
        this.addEventListener('animationend', () => {
            this.deleteMessage();
        });
    }

    deleteMessage() {
        // Remove the message element from the DOM
        this.remove();
    }
}

// Define class elements
window.customElements.define('message-box', MessageBox);
})()
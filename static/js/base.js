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
  
  // Define the custom element
  window.customElements.define('message-box', Message);
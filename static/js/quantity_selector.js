class QuantitySelector extends HTMLElement {
	// Custom element to handle the quantity changes on an input.
	constructor() {
		super()
		this.quantityInput = document.getElementById('quantity');
		this.quantityButtons = document.querySelectorAll('button');
		this.quantity = 1;
	}

	// Runs when custom element is added to DOM.
	connectedCallback() {
		// Loops over quantity buttons in element.
		for (let i = 0; i < this.quantityButtons.length; i++) {
			this.quantityButtons[i].addEventListener('click', (e) => {
				e.preventDefault();

				// String to int for later manipulation
				let valueInt = parseInt(this.quantityInput.value);
				this.quantityChange(e.target.id, valueInt, this.quantityInput, this.quantity);
			});
		}
	}
	quantityChange(target_id, intValue, quantityInput, quantity){
	/**
	 * Updates the quantity of the input field based on a series of parameters
	 * @param target_id - The id of the button clicked used to decide if quantity should increase or decrease
	 * @param intValue - The value of the input parse as an interger for calculations
	 * @param quantityInput - The input holding the quantity value in the QuantitySelector element.
	 * @param quantity - the quantity amount to be increase or decerease.
	 * 
	 * */
		if (target_id === 'plus') {
			intValue +=  quantity;
			quantityInput.value = intValue;
		} else {
			// Prevents value to go below 0
			if (intValue === 0) return;

			intValue -=  quantity;
			quantityInput.value = intValue;
		}
	}
}
customElements.define("quantity-selector", QuantitySelector); 
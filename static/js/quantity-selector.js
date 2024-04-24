class QuantitySelector extends HTMLElement {
    constructor() {
        super();
        this.quantityInput = this.querySelector('#quantity');
        this.quantityButtons = this.querySelectorAll('button');
        this.quantity = 1;
    }

    connectedCallback() {
        this.addEventListener('click', (e) => {
            if (e.target.tagName === 'BUTTON') {
                e.preventDefault();
                const increment = e.target.id === 'plus' ? this.quantity : -this.quantity;
                this.quantityInput.value = Math.max(parseInt(this.quantityInput.value) + increment, 1);
            }
        });
    }
}

customElements.define("quantity-selector", QuantitySelector);


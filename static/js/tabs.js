class tabComponent extends HTMLElement {
    constructor() {
        super();
        this.tabButtonArr = this.querySelectorAll('.tab');
    }

    connectedCallback() {
        this.tabButtonArr.forEach(button => {
            button.addEventListener('click', (e) => {
                const content = e.currentTarget.dataset.content;

                // Remove is-active class from all other tab elements
                this.tabButtonArr.forEach(tab => {
                    if (tab !== e.currentTarget) {
                        tab.classList.remove('is-active');
                    }
                });

                // Add is-active class to the clicked tab
                e.currentTarget.classList.add('is-active');

                // Update content
                this.children[1].innerHTML = `<p class="is-size-6">${content}</p>`;
            });
        });
    }
}

customElements.define("tab-component", tabComponent);

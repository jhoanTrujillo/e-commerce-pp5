document.addEventListener('DOMContentLoaded', () => {
    // Target Update buttons
    const productUpdateBtn = document.querySelectorAll('[data-action-type]');
    
    productUpdateBtn.forEach((button) => {
        button.addEventListener('click', (e) => {
            // Prevent default button behavior
            e.preventDefault();
            
            update_cart_form(e);
        });
    });

    const update_cart_form = (e) => {
        // Prevent default form submission behavior
        e.preventDefault();

        const parentForm = e.currentTarget.closest('form');
        
		// Change parent form action to target the appropriate view
        if (e.currentTarget.dataset.actionType === 'remove') {    
            parentForm.action = "delete/";
        } else {
            parentForm.action = "update/";
        }

        // Submit parent form
        parentForm.submit();
    };
});

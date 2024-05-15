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

// Call the functions when the DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
    setupNavbarBurger();
});

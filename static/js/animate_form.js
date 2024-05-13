(() => {
	const addVariantBtn = document.getElementById("add-variant-btn");
	let variantCounter = 0;

	const setupFormSubmitListener = () => {
		const forms = document.querySelectorAll('form');
		let debounceTimer;
		
		forms.forEach(parentForm => {
			const submitButton = parentForm.querySelector('button[type="submit"]');
			const formInputs = parentForm.querySelectorAll('input, select, textarea');

			submitButton.addEventListener('click', (event) => {
				event.preventDefault();
		
				if (debounceTimer) {
					clearTimeout(debounceTimer);
				}
		
				// Add is-skeleton class to the submit button
				submitButton.classList.add('is-skeleton');

				// Add is-skeleton class to all inputs in the form
				formInputs.forEach(input => {
					input.classList.add('is-skeleton');
				});

				debounceTimer = setTimeout(() => {
					parentForm.submit(); // Submit the form after the debounce delay
					// Remove is-skeleton class after form submission
					submitButton.classList.remove('is-skeleton');
					// Remove is-skeleton class from all inputs in the form after form submission
					formInputs.forEach(input => {
						input.classList.remove('is-skeleton');
					});
				}, 500);
			});
		});
	};

	// Function calls
	setupFormSubmitListener();
})();

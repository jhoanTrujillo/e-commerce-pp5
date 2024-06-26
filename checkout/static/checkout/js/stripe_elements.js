const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// Code taken from stripe style element at https://docs.stripe.com/js/appendix/style
// Creates card and adds style at once
const card = elements.create('card', {
    
});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', (event) => {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
const form = document.getElementById('payment-form');

form.addEventListener('submit', (ev) => {
    ev.preventDefault();

    // Get te data from te form and convert to a easily accessible Json file
    const formData = new FormData(ev.target);
    const formDataJSON = {};
    formData.forEach((value, key) => {
        formDataJSON[key] = value.trim();
    });

    card.update({ 'disabled': true});
    document.getElementById('submit-button').setAttribute('disabled', 'disabled');
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            // billing_details: {
            //     name: formDataJSON.full_name,
            //     phone:  formDataJSON.phone_number,
            //     email: formDataJSON.email,
            //     address: {
            //         line1: formDataJSON.street_address1,
            //         line2: formDataJSON.street_address2,
            //         city: formDataJSON.town_or_city,
            //         country: formDataJSON.country,
            //         state: formDataJSON.county,
            //     }
            // },
            // shipping: {
            //     name: formDataJSON.full_name,
            //     phone:  formDataJSON.phone_number,
            //     email: formDataJSON.email,
            //     address: {
            //         line1: formDataJSON.street_address1,
            //         line2: formDataJSON.street_address2,
            //         city: formDataJSON.town_or_city,
            //         country: formDataJSON.country,
            //         state: formDataJSON.county,
            //         postal_code: formDataJSON.postcode,
            //     }
            // },
        }
    }).then((result) => {
        if (result.error) {
            const errorDiv = document.getElementById('card-errors');
            const html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>
            `;
            errorDiv.innerHTML = html;
            card.update({ 'disabled': false});
            document.getElementById('submit-button').removeAttribute('disabled');
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});


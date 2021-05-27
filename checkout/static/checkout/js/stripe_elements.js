/*
    Source for payment logic:
    https://stripe.com/docs/payments/accept-a-payment

    Source for CSS: 
    https://stripe.com/docs/stripe-js
*/

var StripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var ClientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(StripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        '::placeholder': {
            color: 'e1f5f4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {
    style: style
});
card.mount('#card-element');

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-exclamation-triangle"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handles form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true); //Disahles submit button
    stripe.confirmCardPayment(ClientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false); // Enables submit button to allow user input
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
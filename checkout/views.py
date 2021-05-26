from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IvQ0SDyyvgINJ1Sf73rZogZKD6tYbD8878arLlD8Xn0qBZDYQ0PhQmAxcaXhvXcVMQ11puu2TlismP5XDP2UPLp00S4BnxTBV',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

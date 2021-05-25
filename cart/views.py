from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """ A view to render the shopping cart and contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view to allow products to be added to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """ Edit quantity of specified item in carts  """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

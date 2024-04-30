from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

def view_cart(request):
	"""
	A view to display the cart content
	"""
	return render(request, "cart/cart.html")

def add_to_cart(request):
    """
    Add a product to the cart
    """
    redirect_url = request.POST.get('redirect_url')
    quantity = request.POST.get('quantity')
    
    # Error handling for missing or invalid quantity
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        return HttpResponseBadRequest("Invalid quantity")

    is_variant = 'variant_id' in request.POST
    item_id = request.POST.get('variant_id') if is_variant else request.POST.get('product_id')
    cart = request.session.get('cart', {})

    # Create the cart key
    cart_key = f"variant_{item_id}" if is_variant else f"product_{item_id}"
    
    # Checks if item exists and updates quantity based on outcome
    cart_item = cart.get(cart_key)
    if cart_item:
        cart_quantity = cart_item.get("quantity", 0) + quantity
    else:
        cart_quantity = quantity

    cart[cart_key] = {
        'item_id': item_id,
        'quantity': cart_quantity,
    }

    request.session['cart'] = cart
    return redirect(redirect_url)

def delete_from_cart(request):
    """
    Deletes a product in cart and redirects to cart page
    """
    # Get the item-key value from the cart.html template
    item_key = request.POST.get('item-key')
    
    cart = request.session.get('cart', {})

    # Checks if any item in cart holds the naming convention share in the form
    if item_key in cart:
        # deletes the whole key:value pair from form
        del cart[item_key]
        # updates cart session
        request.session['cart'] = cart

    return redirect('view_cart')

def update_cart_quantity(request):
    """
    Update product quantity in the cart
    """
    # Get the item-key value from the cart.html template
    item_key = request.POST.get('item-key')
    # We convert quantity to int here
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    # Checks if any item in cart holds the naming convention share in the form
    if item_key in cart:
        # Checks for product quantity value and updates quantity
        cart[item_key]['quantity'] = quantity
        # updates cart session
        request.session['cart'] = cart

    return redirect('view_cart')
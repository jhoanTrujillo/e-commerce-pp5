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

    is_variant = request.POST.get('variant_id') is not None
    item_id = request.POST.get('variant_id') if is_variant else request.POST.get('product_id')
    cart = request.session.get('cart', {})

    if cart:
        # Create the key for the key value of the cart dictionary
        cart_key = f"variant_{item_id}" if is_variant else f"product_{item_id}"
        
		# Checks if item exist and updates quantity based on outcome
        if cart_key in cart:
            cart_quantity = cart[cart_key]["quantity"]
            cart_quantity += quantity
        else:
            cart_quantity = quantity
    else:
        cart_quantity = quantity

    cart_item = {
        'item_id': item_id,
        'quantity': cart_quantity,
    }

    cart[cart_key] = cart_item
    request.session['cart'] = cart
    return redirect(redirect_url)

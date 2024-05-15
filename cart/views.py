from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseBadRequest
from products.models import Product, Variant

def view_cart(request):
    """
    A view to display the cart content
    """
    latest_products = Product.objects.order_by('-created_date')[:3]

    context = {
        'latest_products' : latest_products
    }

    return render(request, "cart/cart.html", context)

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
    # Create the cart item key
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

    if is_variant:
        product_or_variant = get_object_or_404(Variant, pk=item_id)
    else:
        product_or_variant = get_object_or_404(Product, pk=item_id)
        
    messages.success(request, f'{quantity} x { product_or_variant } added to cart')
    return redirect(redirect_url)

def delete_from_cart(request):
    item_key = request.POST.get('item-key')
    cart = request.session.get('cart', {})

    deleted_product_title = ""

    if item_key in cart:
        if "variant" in item_key:
            variant_id = int(item_key.split("_")[1])  # Convert to int
            variant = get_object_or_404(Variant, id=variant_id)
            deleted_product_title = variant.product.title
        else:
            product_id = int(item_key.split("_")[1])  # Convert to int
            product = get_object_or_404(Product, id=product_id)
            deleted_product_title = product.title

        del cart[item_key]
        request.session['cart'] = cart

    if deleted_product_title:
        messages.success(request, f'{deleted_product_title} was removed from your cart')
    else:
        messages.success(request, f'An item was removed from your cart')

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
        
        # Add success message
        success_message = ""
        # Check if the item_key contains the word "variant"
        if "variant" in item_key:
            # Extract the variant_id from the item_key
            variant_id = item_key.split("_")[1]
            # Get the variant object
            variant = get_object_or_404(Variant, id=variant_id)
            # Construct success message
            success_message = f"{variant.product.title} changed quantity to {quantity}"
        elif "product" in item_key:
            # Extract the product_id from the item_key
            product_id = item_key.split("_")[1]
            # Get the product object
            product = get_object_or_404(Product, id=product_id)
            # Construct success message
            success_message = f"{product.title} changed quantity to {quantity}"

        # updates cart session
        request.session['cart'] = cart

        # Add success message using Django messages framework
        messages.success(request, success_message)

    # Redirect
    return redirect('view_cart')
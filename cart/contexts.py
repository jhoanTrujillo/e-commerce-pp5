from django.shortcuts import get_object_or_404
from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings
from products.models import Product, Variant

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for cart_key, cart_data in cart.items():
        item_id = cart_data['item_id']
        quantity = cart_data['quantity']
        
        # Fetch the appropriate product or variant
        if 'variant' in cart_key:
            is_variant = True
            product_or_variant = get_object_or_404(Variant, pk=item_id)
        else:
            is_variant = False
            product_or_variant = get_object_or_404(Product, pk=item_id)
        
        added_total = product_or_variant.price * quantity
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product_or_variant': product_or_variant,
            'added_total': added_total,
            'is_variant' : is_variant,
        })

    for item in cart_items:
        total += item['product_or_variant'].price * item['quantity']

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    # Ensure values are rounded to a maximum of 2 decimal points
    shortened_grand_total = Decimal(str(grand_total)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': shortened_grand_total,
    }

    return context
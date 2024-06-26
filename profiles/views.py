from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

@login_required
def profile(request):
	""" Display user's profile """
	profile = get_object_or_404(UserProfile, user=request.user)
	
	form = UserProfileForm(instance=profile)
	orders = profile.orders.all()

	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'profile updated successfully.')

	template = 'profiles/profile.html'
	context = {
		'form' : form,
		'orders' : orders,
	}
	
	return render(request, template, context)

@login_required
def order_history(request, order_number):
	""" Display pass orders for authenticated users """
	order = get_object_or_404(Order, order_number=order_number)
	line_items = [] 

	# Creates boolean value to check if line items exist
	product_line_items_exist = order.productlineitem.exists()
	variant_line_items_exist = order.variantlineitem.exists()

	# If they do adds them to an array
	if product_line_items_exist or variant_line_items_exist:
		if product_line_items_exist:
			line_items += list(order.productlineitem.all())
		if variant_line_items_exist:
			line_items += list(order.variantlineitem.all())
	else:
		pass

	messages.info(request, (
		f'This is a past confirmation for order {order.order_number}.'
		'A confirmation email was sent on the date of the purchase.'
	))

	template = 'checkout/checkout_success.html'
	context = {
		'order': order,
		'line_items': line_items,
		'from_profile': True,
	}

	return render(request, template, context)
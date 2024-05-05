from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

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

def order_history(request, order_number):
	order = get_object_or_404(Order, order_number=order_number)

	messages.info(request, (
		f'This is a past confirmation for order {order.order_number}.'
		'A confirmation email was sent on the date of the purchase.'
	))

	template = 'checkout/checkout_success.html'
	context = {
		'order': order,
		'from_profile' : True,
	}

	return render(request, template, context)
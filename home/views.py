from django.shortcuts import render
from products.models import Product, Collection
from home.forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
	"""
	Homepage view
	"""
	# Querying the three latest products. Used in the latest products section the index.html
	latest_products = Product.objects.order_by('-created_date')[:3]

	# Querying all products in the enamel pins collection
	enamel_pins = Product.objects.filter(collection='1')
	collections = Collection.objects.all()[:2]

	context = {
		'latest_products': latest_products,
		'enamel_pins': enamel_pins,
		'collections' : collections,
	}

	return render(request, "home/index.html", context)

def contact_page(request):
	"""
	View to the contact form of the site
	"""
	submitted = False
	# Checks if request is a post and saves form
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contact?submitted=True')
	
	# Creates new form class and adds placeholders
	form = ContactForm()
	if 'submitted' in request.GET:
		submitted = True

	context = {
		'form' : form,
		'Submitted' : submitted,
	}

	return render(request, "home/contact.html", context)
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Collection


def all_products(request):
	"""
	Show all products with sorting and search query.
	"""
	products = Product.objects.all()
	query = None
	collection = None

	# Checks for a get request
	if request.GET:
		if 'collection' in request.GET:
			collections = request.GET['collection'].split(',')
			products = products.filter(collection__name__in=collections)
			collections = Collection.objects.filter(name__in=collections)

		if 'q' in request.GET:
			query = request.GET['q']
			if not query:
				messages.error(request, "You didn't enter any search criteria")
				return redirect(reverse('products'))

			queries = Q(title__icontains=query) | Q(description__icontains=query)
			products = products.filter(queries)

	context = {
		'products': products,
		'search_term': query,
		'current_collections': collection,
	}

	return render(request, "products/products.html", context)

def product_details(request, product_id):
	"""
	A page that display the details of the each product.
	"""
	product = get_object_or_404(Product, pk=product_id)
	# We get all products except from the currently visible product
	recommended_products = Product.objects.filter(collection=1).exclude(id=product_id)

	context = {
		'recommended_products': recommended_products,
		'product': product,
	}

	return render(request, "products/product_details.html", context)
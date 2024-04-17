from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
	"""
	Show all products with sorting and search query.
	"""
	products = Product.objects.all()

	context = {
		'products': products,
	}

	return render(request, "products/products.html", context)

def product_details(request, product_id):
	"""
	A page that display the details of the each product.
	"""
	product = get_object_or_404(Product, pk=product_id)
	products = Product.objects.filter(collection=1).exclude(id=product_id)

	context = {
		'recommended_products': products,
		'product': product,
	}

	return render(request, "products/product_details.html", context)
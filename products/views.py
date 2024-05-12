from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Prefetch
from .models import Product, Collection, Variant
from .forms import ProductForm, VariantForm

def all_products(request):
    """
    Show all products with sorting and search query.
    """
    products = Product.objects.all().prefetch_related(
        Prefetch('variant_set', queryset=Variant.objects.select_related('product'))
    )
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
	variants = Variant.objects.filter(product=product)
	# We get all products except from the currently visible product
	recommended_products = Product.objects.filter(collection=1).exclude(id=product_id)

	context = {
		'product': product,
		'variants' : variants,
		'recommended_products': recommended_products,
	}

	return render(request, "products/product_details.html", context)

def variant_details(request, product_id, variant_id):
	"""
	A page that display the details of the each product.
	"""
	product = get_object_or_404(Product, pk=product_id)
	variant = get_object_or_404(Variant, pk=variant_id)
	variants = Variant.objects.filter(product=product)
	# We get all products except from the currently visible product
	recommended_products = Product.objects.filter(collection=1).exclude(id=product_id)

	context = {
		'product': product,
		'variants' : variants,
		'variant' : variant,
		'recommended_products': recommended_products,
	}

	return render(request, "products/product_details.html", context)

@login_required
def add_product_or_variant(request):
	""" Add a product or variant to the store"""
	if not request.user.is_superuser:
		messages.failed(request, 'Your account don\'t count with the permission required')
		return redirect(reverse('home'))

	# If post generate both forms in one page
	if request.method == 'POST':
		product_form = ProductForm(request.POST, request.FILES)
		variant_form = VariantForm(request.POST, request.FILES)

		if variant_form.is_valid():  
			variant_instance = variant_form.save()  
			messages.success(request, 'Successfully added variant!')
			product_id = variant_instance.product.id
			variant_id = variant_instance.id
			return redirect('variant_details', product_id=product_id, variant_id=variant_id)
		elif product_form.is_valid():  
			product_instance = product_form.save()  
			messages.success(request, 'Successfully added product!')
			return redirect('product_details', product_id=product_instance.id)
		else:
			messages.error(request, 'Failed to add product or variant. Please ensure the form is valid.')

	else:
		product_form = ProductForm()
		variant_form = VariantForm()  # Initialize an empty variant form

	template = 'products/add_product.html'
	context = {
		'product_form': product_form,
		'variant_form': variant_form,
	}

	return render(request, template, context)

@login_required
def edit_product_or_variant(request, item_id):
	""" Edit a product or variant in the store """
	if not request.user.is_superuser:
		messages.failed(request, 'Your account don\'t count wit the permission required')
		return redirect(reverse('home'))

	is_variant = request.GET.get('is-variant', False)
	if is_variant:
		product_or_variant = get_object_or_404(Variant, pk=item_id)
	else:
		product_or_variant = get_object_or_404(Product, pk=item_id)

	if request.method == 'POST':
		if is_variant:
			form = VariantForm(request.POST, request.FILES, instance=product_or_variant)
		else:
			form = ProductForm(request.POST, request.FILES, instance=product_or_variant)

		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully updated product!')
			if is_variant:
				product_id = product_or_variant.product.id
				variant_id = product_or_variant.id
				return redirect(reverse('variant_details', args=[product_id, variant_id]))
			else:
				return redirect('product_details', product_id=product_or_variant.id)
		else:
			# If form is invalid, add error messages
			messages.error(request, 'Failed to update product. Please correct the errors in the form.')
	else:
		if is_variant:
			form = VariantForm(instance=product_or_variant)
		else:
			form = ProductForm(instance=product_or_variant)
		messages.info(request, f'You are editing {product_or_variant.title}')

	template = 'products/edit_product_or_variant.html'
	context = {
		'form': form,
		'item': product_or_variant,
		'is_variant': is_variant,
	}

	return render(request, template, context)

@login_required
def delete_product_or_variant(request, item_id):
	""" Delete a product or variant from the store """
	if not request.user.is_superuser:
		messages.error(request, 'Your account doesn\'t have the required permission')
		return redirect('home')

	is_variant = request.GET.get('is-variant', False)

	if is_variant:
		product_or_variant = get_object_or_404(Variant, pk=item_id)
		print(f"Variant ID: {item_id}")
	else:
		product_or_variant = get_object_or_404(Product, pk=item_id)
		print(f"Product ID: {item_id}")

	try:
		product_or_variant.delete()
		messages.success(request, 'Successfully deleted product or variant!')
	except Exception as e:
		messages.error(request, 'Unable to delete product or variant. Please try again.')
		print(f"Exception: {e}")

	return redirect('products')
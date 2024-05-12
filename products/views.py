from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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

def add_product_or_variant(request):
	""" Add a product or variant to the store"""
	# If post generate both forms in one page
	if request.method == 'POST':
		product_form = ProductForm(request.POST, request.FILES)
		variant_form = VariantForm(request.POST, request.FILES)

		if variant_form.is_valid():  # Check if variant form is valid
			variant_instance = variant_form.save()  # Save variant form (product association will be handled automatically)
			messages.success(request, 'Successfully added variant!')
			return redirect('add_product')  # Redirect to the same page after successfully adding a variant
		elif product_form.is_valid():  # Check if product form is valid
			product_instance = product_form.save()  # Save product form
			messages.success(request, 'Successfully added product!')
			return redirect('add_product')  # Redirect to the same page after successfully adding a product
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


def edit_product_or_variant(request, item_id):
	""" Edit a product or variant in the store """
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
				product_id=product_or_variant.product.id
				variant_id=product_or_variant.id
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

def delete_product_or_variant(request, item_id):
	""" Delete a product or variant from the store """
	is_variant = request.GET.get('is_variant', False)

	if is_variant:
		product_or_variant = get_object_or_404(Variant, pk=item_id)
	else:
		product_or_variant = get_object_or_404(Product, pk=item_id)
	try:
		product_or_variant.delete()
		messages.success(request, 'Successfully deleted product or variant!')
	except Exception as e:
		messages.error(request, 'Unable to delete product or variant. Please try again.')

	return redirect(reverse('products'))  # Redirect to the product list page after deleting a product or a variant
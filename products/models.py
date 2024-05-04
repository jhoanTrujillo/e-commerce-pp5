from django.db import models

class Collection(models.Model):
	name =  models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True)
	user_friendly_name = models.CharField(max_length=100)
	description = models.TextField()
	
	# Returns a more readable name for products
	def __str__(self):
		return self.name
	
	def get_friendly_name(self):
		return self.user_friendly_name

class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField() 
	sku = models.CharField(max_length=100, null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(null=True, blank=True)
	image_url = models.URLField(max_length=1024, null=True, blank=True)
	rating = models.DecimalField(max_digits=6, decimal_places=2)
	collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
	stock = models.IntegerField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	# Returns a more readable name for products
	def __str__(self):
		return self.title

class Variant(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(null=True, blank=True)
	image_url = models.URLField(max_length=1024, null=True, blank=True)
	stock = models.IntegerField()

	# Returns a more readable name for variants
	def __str__(self):
		return self.title

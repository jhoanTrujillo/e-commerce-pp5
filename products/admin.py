from django.contrib import admin
from .models import Product, Collection, Variant

# Register your models here.
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Variant)
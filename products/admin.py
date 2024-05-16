from django.contrib import admin
from .models import Product, Collection, Variant


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'collection',
        'price',
        'stock',
        'image',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'stock'
        'image',
    )

    ordering = ('title',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'user_friendly_name',
        'name',
    )

    ordering = ('user_friendly_name',)

# Register your models here.


admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Variant)

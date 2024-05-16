from django.contrib import admin
from .models import Order, ProductLineItem, VariantLineItem


class OrderProductLineItemAdminInline(admin.TabularInline):
    model = ProductLineItem
    readonly_fields = ('lineitem_total',)


class OrderVariantLineItemAdminInline(admin.TabularInline):
    model = VariantLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderProductLineItemAdminInline, OrderVariantLineItemAdminInline,
         )

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid', 'user_profile')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'user_profile', 'date',
                    'full_name', 'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

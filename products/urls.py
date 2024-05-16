from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('<int:product_id>/variants/<int:variant_id>/', views.variant_details,
         name='variant_details'),
    path('add/', views.add_product_or_variant, name='add_product_or_variant'),
    path('edit/<int:item_id>', views.edit_product_or_variant, name='edit'),
    path('delete/<int:item_id>', views.delete_product_or_variant,
         name='delete_product_or_variant')
]

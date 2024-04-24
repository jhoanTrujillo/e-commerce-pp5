from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.all_products, name='products'),
	path('<int:product_id>/', views.product_details, name='product_details'),
	path('<int:product_id>/variants/<int:variant_id>', views.variant_details, name='variant_details')
]
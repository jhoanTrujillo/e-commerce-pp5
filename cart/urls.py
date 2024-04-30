from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
	path('add/', views.add_to_cart, name='add_to_cart'),
	path('delete/', views.delete_from_cart, name='delete_from_cart'),
	path('update/', views.update_cart_quantity, name='update_cart_quantity')
] 
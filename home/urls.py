from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_page, name='contact_page'),
    path('about/', views.about, name='about'),
]

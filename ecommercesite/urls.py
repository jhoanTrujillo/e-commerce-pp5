from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('home.urls')),
	
	# URL path needed by allauth
	path('accounts/', include('allauth.urls')),
]

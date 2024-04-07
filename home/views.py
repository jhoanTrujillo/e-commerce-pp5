from django.shortcuts import render

# Create your views here.
def home(request):
	"""
	Homepage view
	"""
	return render(request, "home/index.html")
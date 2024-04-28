from django.shortcuts import render
from home.forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
	"""
	Homepage view
	"""
	return render(request, "home/index.html")

def contact_page(request):
	"""
	View to the contact form of the site
	"""
	submitted = False
	# Checks if request is a post and saves form
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contact?submitted=True')
	
	# Creates new form class and adds placeholders
	form = ContactForm()
	if 'submitted' in request.GET:
		submitted = True

	context = {
		'form' : form,
		'Submitted' : submitted,
	}

	return render(request, "home/contact.html", context)
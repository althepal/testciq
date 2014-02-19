from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
			'title': 'CultureIQ - DEV',
			}
	template = 'index.html'
	return render(request, template, context)

def customer(request):
	context = {
			'title': 'CultureIQ - DEV - ',
			}
	template = 'customer.html'
	return render(request, template, context)


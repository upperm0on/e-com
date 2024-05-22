from django.shortcuts import render, redirect

from .models import product
from .forms import Product_form

# Create your views here.
def first_view(request): 
	context = {
	}
	return render(request, 'index.html', context)

def create(request): 
	form = Product_form(request.POST or None) 
	if request.method == "POST": 
		if form.is_valid: 
			form.save()
			print(form.cleaned_data)
			form = Product_form()
	context = {
		'form' : form, 
	}
	return render(request, "products/create.html", context)

def read(request):
	obj = product.objects.all() 
	context = {
		'object' : obj,
	}
	return render(request, "products/read.html", context)

def details(request, id): 
	obj = product.objects.get(id=id)
	context = {
		'object' : obj, 
	}
	return render(request, "products/details.html", context)

def update(request, id): 
	obj = product.objects.get(id=id) 
	form = Product_form(request.POST or None, instance=obj)
	if request.method == "POST": 
		if form.is_valid(): 
			form.save()
			return redirect('/products/read/')
	context = {
		"form" : form, 
	}
	return render(request, "products/update.html", context)

def delete(request, id): 
	obj = product.objects.get(id=id) 
	obj.delete() 
	return redirect('/products/read/')
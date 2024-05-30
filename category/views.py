from django.shortcuts import render, redirect
from .models import category
from base_app.models import product 

from .form import Category_form  
# Create your views here.

def create(request): 
	form = Category_form(request.POST or None) 
	if request.method == "POST": 
		if form.is_valid: 
			form.save()
			form = Category_form()
	context = {
		'form' : form, 
	}
	return render(request, "category/create.html", context)

def read(request):
	obj = category.objects.all() 
	context = {
		'object' : obj,
	}
	return render(request, "category/read.html", context)

def details(request, id): 
	cat_obj = category.objects.get(id=id)
	obj = product.objects.filter(category=id)
	context = {
		'object' : obj,
		'cat_obj' : cat_obj, 
	}
	return render(request, "category/details.html", context)

def update(request, id): 
	obj = category.objects.get(id=id) 
	form = Category_form(request.POST or None, instance=obj)
	if request.method == "POST": 
		if form.is_valid(): 
			form.save()
			return redirect('/category/read/')
	context = {
		"form" : form, 
	}
	return render(request, "category/update.html", context)

def delete(request, id): 
	obj = category.objects.get(id=id) 
	obj.delete() 
	return redirect('/category/read/')
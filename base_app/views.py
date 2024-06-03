from django.shortcuts import render, redirect

from .models import product
from .forms import Product_form
from review.models import review

from ratings.models import (
	five_star,
	four_star,
	three_star,
	two_star,
	one_star
)

# Create your views here.
def first_view(request): 
	context = {
	}
	return render(request, 'index.html', context)

def create(request): 
	form = Product_form 
	if request.method == "POST": 
		form = Product_form(request.POST or None, request.FILES)
		if form.is_valid: 
			form.save(commit=True)
			form = Product_form()
	context = {
		'form' : form, 
	}
	return render(request, "products/create.html", context)

def read(request):
	obj = product.objects.all().order_by("-date_added")
	context = {
		'object' : obj,
	}
	return render(request, "products/read.html", context)

def details(request, id): 
	obj = product.objects.get(id=id)
	stars_list = [one_star, two_star, three_star, four_star, five_star]
	reviews = review.objects.filter(product=obj).all().order_by("-date_added")

	if request.method == "POST": 
		model_no = int(request.POST['star-selection']) 
		stars_list[model_no - 1].objects.create(product=obj)

		comment = request.POST['review_text']

		review.objects.create(product=obj, comment=comment)

	total_star = 0 
	count2 = 0
	for i in range(len(stars_list)):
		count = stars_list[i].objects.filter(product=obj).count()
		counted_rate = stars_list[i].objects.filter(product=obj).count()
		count2 += counted_rate

		count = count * (i + 1) 
		total_star += count

	try: 
		total_rate = (total_star/count2) 
	except: 
		total_rate = 0


	context = {
		'object' : obj, 
		'total_rate': round(total_rate, 1),
		'counted_stars': count2,
		'reviews' : reviews,
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
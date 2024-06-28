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

# View for rendering the dashboard page
def dashboard(request): 
    context = {}
    return render(request, 'dashboard.html', context)

# View for rendering the index page
def first_view(request): 
    context = {}
    return render(request, 'index.html', context)

# View for creating a new product
def create(request): 
    form = Product_form()  # Initialize the product form
    if request.method == "POST": 
        form = Product_form(request.POST or None, request.FILES)  # Bind form data to the form
        if form.is_valid(): 
            form.save(commit=True)  # Save the form data to the database
            form = Product_form()  # Reinitialize the form after saving
    context = {
        'form' : form, 
    }
    return render(request, "products/create.html", context)

# View for reading and displaying all products
def read(request):
    obj = product.objects.all().order_by("-date_added")  # Get all products ordered by the date added
    context = {
        'object' : obj,
    }
    return render(request, "products/read.html", context)

# View for displaying the details of a single product
def details(request, id): 
    obj = product.objects.get(id=id)  # Get the product by ID
    stars_list = [one_star, two_star, three_star, four_star, five_star]  # List of star rating models
    reviews = review.objects.filter(product=obj).all().order_by("-date_added")  # Get all reviews for the product

    if request.method == "POST": 
        model_no = int(request.POST['star-selection'])  # Get the selected star rating
        stars_list[model_no - 1].objects.create(product=obj)  # Create a star rating entry

        comment = request.POST['review_text']  # Get the review comment
        review.objects.create(product=obj, comment=comment)  # Create a review entry

    total_star = 0 
    count2 = 0
    # Calculate the total star rating and count
    for i in range(len(stars_list)):
        count = stars_list[i].objects.filter(product=obj).count()
        counted_rate = stars_list[i].objects.filter(product=obj).count()
        count2 += counted_rate

        count = count * (i + 1) 
        total_star += count

    # Calculate the average rating
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

# View for updating an existing product
def update(request, id): 
    obj = product.objects.get(id=id)  # Get the product by ID
    form = Product_form(instance=obj)  # Initialize the form with the existing product data
    if request.method == "POST":
        form = Product_form(request.POST, request.FILES, instance=obj)  # Bind form data to the form
        if form.is_valid(): 
            form.save()  # Save the updated product data to the database
            return redirect('/products/read/')  # Redirect to the products read view
    context = {
        "form" : form, 
    }
    return render(request, "products/update.html", context)

# View for deleting an existing product
def delete(request, id): 
    obj = product.objects.get(id=id)  # Get the product by ID
    obj.delete()  # Delete the product
    return redirect('/products/read/')  # Redirect to the products read view

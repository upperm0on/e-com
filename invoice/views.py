from django.shortcuts import render, redirect
from .forms import ViewInvoiceForms
from base_app.models import product

def create_invoice(request):
    # Initialize form, obj (search results), and transformed_objects (to display in template)
    form = ViewInvoiceForms()
    obj = None
    transformed_objects = []

    # Handle form submission (POST request)
    if request.method == "POST":
        form = ViewInvoiceForms(request.POST)

        # Handle item search form submission
        if 'item_search_btn' in request.POST:
            search_query = request.POST.get('item_search')
            # Filter products based on search query
            obj = product.objects.filter(name__icontains=search_query)

        # Handle starting a new invoice (clear objects_list in session)
        if 'new_invoice' in request.POST:
            request.session['objects_list'] = []
            return redirect('create_invoice')  # Redirect to clear form and session

        # Retrieve objects_list from session or initialize empty list
        objects_list = request.session.get('objects_list', [])

        # Handle adding an item to the invoice
        if 'add_item' in request.POST:
            hidden_value = int(request.POST.get('hidden_value'))
            
            # Check if the item ID is not already in objects_list to avoid duplicates
            if hidden_value not in objects_list:
                objects_list.append(hidden_value)
                # Update objects_list in session
                request.session['objects_list'] = objects_list

        # Handle clearing all items from the invoice
        if 'clear_items' in request.POST:
            request.session['objects_list'] = []  # Clear all items in objects_list

    # Retrieve objects_list from session after processing POST requests
    objects_list = request.session.get('objects_list', [])

    # Fetch products based on IDs in objects_list to display in the invoice
    transformed_objects = product.objects.filter(id__in=objects_list)

    # Prepare context to pass to the template
    context = {
        'invoice_form': form,        # Form for searching and adding items
        'object': obj,               # Search results (filtered products)
        'objects_list': transformed_objects,  # Products to display in the invoice
    }

    # Render the template with the context
    return render(request, 'invoice/create_invoice.html', context)

from django.shortcuts import render
from base_app.models import product as Product
from django.db.models.functions import ExtractYear
from django.db.models import IntegerField
from invoice.models import Invoice
import json
from datetime import datetime

def dashboard(request):
    # Get the current year
    current_year = datetime.now().year

    # Fetch available years from the database
    available_years = Product.objects.annotate(
        year=ExtractYear('date_added', output_field=IntegerField())
    ).values_list('year', flat=True).distinct()
    available_years_list = list(available_years)

    # Define months and initialize revenues
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_revenues = {month: 0 for month in months}

    # Determine the year to use based on form submission or default to current year
    year = request.POST.get('year', current_year)

    # Fetch and process invoice data for the selected year
    invoice_objects = Invoice.objects.filter(date_created__year=year)

    for invoice in invoice_objects:
        invoice_data = invoice.items
        
        for item in invoice_data.values():
            quantity = float(item.get("Quantity", 0))
            price = float(item.get("Price", 0))
            income = quantity * price
            
            invoice_date = invoice.date_created
            month_name = months[invoice_date.month - 1]
            
            month_revenues[month_name] += income

    # Round revenues and prepare JSON data
    month_revenues = {month: round(revenue, 2) for month, revenue in month_revenues.items()}
    revenue_list = [{'month': month, 'value': month_revenues[month]} for month in months]
    revenue_json = json.dumps(revenue_list)

    context = {
        'years': available_years_list,
        'revenue': revenue_json,
        'selected_year': year,  # Pass the selected year to the template
    }
    return render(request, 'dashboard/dashboard.html', context)

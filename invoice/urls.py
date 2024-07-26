from .views import create_invoice, read_invoice, details_invoice

from django.urls import path

urlpatterns = [
	path('create_invoice/', create_invoice, name="create_invoice"),
	path('read_invoice/', read_invoice, name="read_invoice"),
	path('details_invoice/<int:id>/', details_invoice, name="details_invoice")
]
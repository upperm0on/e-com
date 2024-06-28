from .views import create_invoice 

from django.urls import path

urlpatterns = [
	path('create_invoice/', create_invoice, name="create_invoice")
]
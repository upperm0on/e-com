from django.urls import path 
from . import views

urlpatterns = [
	path('', views.first_view, name="landing_page"),
	path('read/', views.read, name="products_read"),
	path('details/<int:id>/', views.details, name="products_details"),
	path('create/', views.create, name="products_create"),
	path('update/<int:id>/', views.update, name="products_update"),
	path('delete/<int:id>/', views.delete, name="products_delete"),
]
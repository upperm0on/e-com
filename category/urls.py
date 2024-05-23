from django.urls import path 
from . import views

urlpatterns = [
	path('read/', views.read, name="category_read"),
	path('details/<int:id>/', views.details, name="category_details"),
	path('create/', views.create, name="category_create"),
	path('update/<int:id>/', views.update, name="category_update"),
	path('delete/<int:id>/', views.delete, name="category_delete"),
]
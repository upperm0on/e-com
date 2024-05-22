from .models import product 

from django import forms 

class Product_form(forms.ModelForm): 
	class Meta: 
		model = product 
		fields = [
			'name',
			'price',
			'quantity',
			'status',
			'category'
		]
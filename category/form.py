from .models import category 

from django import forms 

class Category_form(forms.ModelForm): 
	class Meta: 
		model = category 
		fields = [
			'name',
			'status',
		]
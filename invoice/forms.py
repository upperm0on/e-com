from django import forms
from .models import Invoice


class ViewInvoiceForms(forms.ModelForm): 
	class Meta: 
		model = Invoice 
		fields = ['items']
		
from django.db import models
from base_app.models import product


# Create your models here.
class review(models.Model): 
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	comment = models.TextField(null=True) 
	date_added = models.DateTimeField(auto_now=True)
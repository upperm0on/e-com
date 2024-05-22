from django.db import models
from category.models import category

# Create your models here.
class product(models.Model): 
	name 		= models.CharField(max_length=240)
	price 		= models.CharField(max_length=240)
	quantity 	= models.IntegerField()
	CHOICES = [('Available', 'Available'), ('Out of Stock', 'Out of Stock')]
	status 		= models.CharField(max_length=240, default='Available', choices=CHOICES)
	category 	= models.ForeignKey(category, on_delete=models.CASCADE)

	def __str__(self): 
		return self.name 
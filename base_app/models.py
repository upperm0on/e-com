from django.db import models
from category.models import category
import datetime 

# Create your models here.
class product(models.Model): 
	name 		= models.CharField(max_length=240)
	price 		= models.CharField(max_length=240)
	quantity 	= models.IntegerField()
	CHOICES = [('Available', 'Available'), ('Out of Stock', 'Out of Stock')]
	status 		= models.CharField(max_length=240, default='Available', choices=CHOICES)
	category 	= models.ForeignKey(category, on_delete=models.CASCADE)
	date_added  = models.DateTimeField(null=True, auto_now_add=True)
	details 	= models.TextField(null=True)
	product_image = models.ImageField(null=True, upload_to="media/")

	def check_quantity(self):
		if self.quantity <= 0: 
			self.status = 'Out of Stock'
			self.quantity = 0
		else: 
			self.status = 'Available'
		return self.status


	def __str__(self): 
		return self.name
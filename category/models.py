from django.db import models

# Create your models here.
class category(models.Model): 
	name 		= models.CharField(max_length=240) 
	CHOICES = [('Available', 'Available'), ('Unavailable', 'Unavailable')]
	status 		= models.CharField(max_length=240, default="Unavailable", choices=CHOICES) 

	def __str__(self): 
		return self.name 
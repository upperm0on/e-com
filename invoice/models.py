from django.db import models

# Create your models here.
class Invoice(models.Model): 
	date_created = models.DateTimeField(auto_now_add=True)
	items = models.JSONField()
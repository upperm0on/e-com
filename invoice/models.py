from django.db import models
from datetime import datetime

class Invoice(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    items = models.JSONField()

    def formatted_date(self):
        day = self.date_created.day
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]

        return self.date_created.strftime(f'%A, %B {day}{suffix}, %Y, %I:%M %p')

    def __str__(self):
        return f"Invoice created on {self.formatted_date()}"

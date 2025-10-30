# events/models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # e.g. 4.7
    cost = models.DecimalField(max_digits=8, decimal_places=2)     # e.g. 59.99
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title

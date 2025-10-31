# events/models.py
from django.db import models
from django.utils import timezone
from django.db.models import Avg

class Event(models.Model):
    GROUP_CHOICES = [
        ('haunt', 'Haunting'),
        ('feast', 'Feasting'),
        ('possess', 'Possession'),
        ('cult', 'Cult Activities'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)  # average rating
    cost = models.DecimalField(max_digits=8, decimal_places=2)     # e.g. 59.99
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, default='haunt')

    def __str__(self):
        return self.title

    def update_average_rating(self):
        """Recalculate and store the average rating."""
        avg = self.ratings.aggregate(avg=Avg('rating'))['avg']
        self.rating = round(avg, 1) if avg else 0
        self.save(update_fields=['rating'])


class Rating(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.rating}★ for {self.event.title}"

    def save(self, *args, **kwargs):
        """Save and update parent event’s average rating."""
        super().save(*args, **kwargs)
        self.event.update_average_rating()

    class Meta:
        ordering = ['-created_at']
# events/admin.py
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'cost', 'rating')
    search_fields = ('title', 'location', 'description')

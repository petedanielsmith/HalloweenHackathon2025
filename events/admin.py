# events/admin.py
from django.contrib import admin
from .models import Event, Rating

class RatingInline(admin.TabularInline):  # or StackedInline for full form layout
    model = Rating
    extra = 1  # show one empty form by default
    fields = ('name', 'rating', 'text', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'location', 'cost', 'rating')
    list_filter = ('group',)
    inlines = [RatingInline]
    readonly_fields = ('rating',)
    search_fields = ('title', 'location', 'description')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('event__title', 'name')
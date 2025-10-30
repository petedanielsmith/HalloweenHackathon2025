# events/views.py
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Event

def home(request):
    return render(request, 'events/home.html')

def about(request):
    return render(request, 'events/about.html')

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 6  # set your page size

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

def purchase(request, pk):
    event = get_object_or_404(Event, pk=pk)
    # Show a dummy payment page (no real processing)
    return render(request, 'events/purchase.html', {'event': event})

def checkout(request):
    if request.method == 'POST':
        # Grab submitted dummy data (ignored in real life)
        event_id = request.POST.get('event_id')
        # …you could validate or log here…
        return redirect('checkout_success')
    # If someone navigates directly here, just bounce them home
    return redirect('home')

def checkout_success(request):
    return render(request, 'events/checkout_success.html')

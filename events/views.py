# events/views.py
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Event
from django.db.models import Count, Avg
from django.db.models import Q
from django.utils.http import urlencode
import random

def home(request):
    return render(request, 'events/home.html')

def about(request):
    return render(request, 'events/about.html')

def faq(request):
    return render(request, 'events/faq.html')

def privacy(request):
    return render(request, 'events/privacy.html')

def terms(request):
    return render(request, 'events/terms.html')

def contact(request):
    centuries = list(range(15, 22))  # 15 → 21
    return render(request, 'events/contact.html', {'centuries': centuries})

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 6

    def get_queryset(self):
        queryset = Event.objects.all()
        q = self.request.GET.get('q')
        min_rating = self.request.GET.get('min_rating')
        max_cost = self.request.GET.get('max_cost')
        group = self.request.GET.get('group')

        if q:
            queryset = queryset.filter(title__icontains=q) | queryset.filter(location__icontains=q)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        if max_cost:
            queryset = queryset.filter(cost__lte=max_cost)
        if group:
            queryset = queryset.filter(group=group)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_choices'] = Event.GROUP_CHOICES
        return context

    def get(self, request, *args, **kwargs):
        """
        Redirect messy querystrings to clean ones.
        Example:
        /events/?page=1&q=&min_rating=&max_cost=
        becomes /events/
        """
        params = {}
        for key, value in request.GET.items():
            if value and not (key == "page" and value == "1"):
                params[key] = value

        clean_query = urlencode(params)

        # If current querystring is different from clean one → redirect
        if request.META.get("QUERY_STRING", "") != clean_query:
            base = request.path
            url = f"{base}?{clean_query}" if clean_query else base
            return redirect(url)

        return super().get(request, *args, **kwargs)

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()

        # All ratings for this event
        ratings = event.ratings.all()

        # Aggregate counts for rating distribution (1–5)
        distribution = (
            ratings.values('rating')
            .annotate(count=Count('rating'))
            .order_by('-rating')
        )

        # Convert to dict for easier template access
        dist_dict = {r['rating']: r['count'] for r in distribution}
        total_reviews = ratings.count()
        avg_rating = ratings.aggregate(avg=Avg('rating'))['avg'] or 0

        context.update({
            'ratings': ratings,
            'total_reviews': total_reviews,
            'avg_rating': round(avg_rating, 2),
            'distribution': dist_dict,
        })
        return context

def purchase(request, pk):
    event = get_object_or_404(Event, pk=pk)
    possible_gifts = [
        "Cauldron of bats",
        "Anti-Garlic Spray",
        'Poltergeist (“we need to get rid...”)',
        "Selection of cursed artifacts",
        "A jack-o'-lantern",
    ]
    # Randomly pick 1 or 2 unique gifts
    num_gifts = random.choice([1, 2])
    free_gifts = random.sample(possible_gifts, num_gifts)
    context = {
        "event": event,
        "free_gifts": free_gifts,
    }
    return render(request, "events/purchase.html", context)

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

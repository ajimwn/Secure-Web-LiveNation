from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Concert

def home(request: HttpRequest) -> HttpResponse:
    """Render the home page with a list of upcoming concerts."""
    # Fetch all concerts from the database, ordered by date
    concerts = Concert.objects.all().order_by('date')
    
    # Package the data to send to the HTML template
    context = {
        'concerts': concerts
    }
    return render(request, 'index.html', context)
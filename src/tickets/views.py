from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Concert, Booking, AuditLog

def home(request: HttpRequest) -> HttpResponse:
    """Render the home page with a list of upcoming concerts."""
    concerts = Concert.objects.all().order_by('date')
    context = {'concerts': concerts}
    return render(request, 'index.html', context)

def register(request: HttpRequest) -> HttpResponse:
    """Secure user registration view."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Account created securely! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def book_ticket(request: HttpRequest, concert_id: str) -> HttpResponse:
    """Securely creates a ticket booking and logs the action."""
    if request.method == 'POST':
        # Safely get the concert, or return a 404 error if tampered with
        concert = get_object_or_404(Concert, id=concert_id)
        
        # Create the booking in the database
        Booking.objects.create(user=request.user, concert=concert)
        
        # SECURITY REQUIREMENT: Write to the Audit Log
        AuditLog.objects.create(
            user=request.user,
            action=f"Booked ticket for {concert.title}",
            ip_address=request.META.get('REMOTE_ADDR')
        )
        
        messages.success(request, f"Successfully booked your ticket for {concert.title}!")
        return redirect('profile')
        
    return redirect('home')

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    """Displays the user's purchased tickets."""
    # Fetch only the bookings that belong to the logged-in user
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'profile.html', {'bookings': bookings})
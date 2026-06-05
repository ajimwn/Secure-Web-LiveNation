from django.contrib import admin
from .models import Concert, Booking, AuditLog

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin): # type: ignore
    # This makes the dashboard look highly professional for your presentation
    list_display = ('title', 'date', 'price')
    search_fields = ('title',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('user', 'concert', 'quantity', 'booking_date')
    list_filter = ('booking_date',)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin): # type: ignore
    # Mandatory requirement dashboard view
    list_display = ('timestamp', 'user', 'action', 'ip_address')
    list_filter = ('timestamp', 'action')
    search_fields = ('user__username', 'action')
from django.contrib import admin
from .models import Concert, Booking, AuditLog

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    """Admin interface for Concert model."""
    pass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin interface for Booking model."""
    pass

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    """Admin interface for AuditLog model."""
    pass
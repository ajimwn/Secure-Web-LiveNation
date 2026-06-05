import uuid
from django.db import models
from django.contrib.auth.models import User

# 1. Concert Model (For Admin CRUD & User browsing)
class Concert(models.Model):
    # SECURITY: Using UUIDs instead of sequential IDs prevents IDOR attacks (OWASP A5)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    # We will secure this file upload later according to the rubric
    poster = models.ImageField(upload_to='posters/', blank=True, null=True) 

    def __str__(self):
        return self.title

# 2. Booking Model (The secure CRUD booking module)
class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.concert.title}"

# 3. Audit Log Model (Mandatory requirement)
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.action}"
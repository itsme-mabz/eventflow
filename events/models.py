from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    venue_name = models.CharField(max_length=255) 
    venue_address = models.TextField() 
    categories = models.ManyToManyField(Category, blank=True)
    organizer_name = models.CharField(max_length=255, null=True, blank=True)
    attendees = models.ManyToManyField(User, related_name='attendees', blank=True)
    ticket_total_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

    def clean(self):
        if self.quantity > self.event.ticket_total_quantity:
            raise ValidationError("Cannot select more tickets than available.")

    def save(self, *args, **kwargs):
        self.available_quantity = self.event.ticket_total_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event.title} - {self.name}"

class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.title} - {self.ticket.name}"

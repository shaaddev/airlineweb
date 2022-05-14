from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse, reverse_lazy

# Create your models here.
PASSENGER_CHOICES =(
    (1, '1'),
    (2, '2'),
    (3, '3'),
)

TRIP_CHOICES = (
    ('Round Trip', 'Round Trip'),
    ('One Way', 'One Way')
)


class Book(models.Model):
    from_field = models.CharField(max_length=100, verbose_name="From")
    to_field = models.CharField(max_length=100, verbose_name="To")
    type_of_trip = models.CharField(max_length=100, choices=TRIP_CHOICES, default='One Way', verbose_name="Trip Type")
    # trip_date = models.DateField(verbose_name="Departure Date")
    passengers = models.IntegerField(choices=PASSENGER_CHOICES, default=1, verbose_name="Passengers") 
    shop_with_roytec = models.BooleanField(verbose_name="Shop with Roytec")
    refundable = models.BooleanField(verbose_name="Refundable Fares")
    date_flex = models.BooleanField(verbose_name="My Dates are Flexible")

    def get_absolute_url(self):
        return reverse('book', kwargs={'pk':self.pk})

    def __str__(self):
        return f"{self.from_field} -> {self.to_field}"



class Contact(models.Model):
    email_address = models.EmailField(default='', verbose_name="*Email Address")
    first_name = models.CharField(max_length=150, verbose_name="*First Name")
    last_name = models.CharField(max_length=150, verbose_name="*Last Name")
    country = models.CharField(max_length=200, verbose_name="*Country")

    def get_absolute_url(self):
        return reverse('contact', kwargs={'pk':self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
                
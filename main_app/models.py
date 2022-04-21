import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

CAR_CHOICES = {
    ("Sedan", "Sedan"),
    ("Hatchback", "Hatchback"),
    ("SUVs", "SUVs"),
    ("Coupes", "Coupes"),
    ("Convertible", "Convertible"),
    ("Trucks", "Trucks"),
    ("Van", "Van"),
    ("Crossovers", "Crossovers"),
    ("Minivans", "Minivans"),
}

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)
# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    image = models.CharField(max_length=300)
    color = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100, choices = CAR_CHOICES)
    available = models.BooleanField(max_length=100, choices = TRUE_FALSE_CHOICES)
    car_contact_name = models.CharField(max_length=200)
    car_contact_email = models.CharField(max_length=254)


    def __str__(self):
        return self.make



class Home(models.Model):

    location = models.CharField(max_length=100)
    home_type = models.CharField(max_length=50)
    amenities = models.CharField(max_length=700)
    image = models.CharField(max_length=300)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=254)
    bedrooms = models.CharField(max_length=200)
    bathrooms = models.CharField(max_length=100)
    available = models.BooleanField(max_length=100, choices = TRUE_FALSE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    car = models.ManyToManyField(Car)

    
    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']
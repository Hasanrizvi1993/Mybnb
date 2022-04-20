from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Home(models.Model):

    location = models.CharField(max_length=100)
    home_type = models.CharField(max_length=50)
    amenities = models.CharField(max_length=700)
    image = models.CharField(max_length=300)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=254)
    bedrooms = models.CharField(max_length=200)
    bathrooms = models.CharField(max_length=100)
    available = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)

    
    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']
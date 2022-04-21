from django.contrib import admin

# Register your models here.
from .models import Home, Car, Review # import the Home model from models.py
# Register your models here.

admin.site.register(Home)
admin.site.register(Car)
admin.site.register(Review)
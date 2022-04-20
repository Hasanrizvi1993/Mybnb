from django.contrib import admin

# Register your models here.
from .models import Home # import the Home model from models.py
# Register your models here.

admin.site.register(Home) # this line will add the model to the admin panel
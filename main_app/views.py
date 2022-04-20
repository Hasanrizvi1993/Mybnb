from re import template
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Home
from django.views.generic.edit import CreateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home_index(TemplateView):
    template_name="home.html"

class About(TemplateView):
    template_name = "about.html"


class HomeList(TemplateView):
    model = Home
    template_name = "homelist.html"

    # context_object_name = 'homes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homes = Home.objects.all()
        context["homes"] = homes # Here we are using the model to query the database for us.
        return context


class Home_Create(CreateView):
    model = Home
    fields = ['location', 'home_type', 'amenities', 'image', 'contact_name', 'contact_email', 'bedrooms', 'available']
    template_name = "home_create.html"
    success_url = "/homes/"

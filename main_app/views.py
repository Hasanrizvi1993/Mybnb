from ast import Delete
from audioop import reverse
from re import template
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Home
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

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
    def get_success_url(self):
        return reverse('home_detail', kwargs={'pk': self.object.pk})


class Home_Detail(DetailView):
    model = Home
    template_name = "home_detail.html"


class Home_Update(UpdateView):
    model = Home
    fields = ['location', 'home_type', 'amenities', 'image', 'contact_name', 'contact_email', 'bedrooms', 'available']
    template_name = "home_update.html"
    def get_success_url(self):
        return reverse('home_detail', kwargs={'pk': self.object.pk})

class Home_Delete(DeleteView):
    model = Home
    template_name = "home_delete_confirmation.html"
    success_url = "/homes/"
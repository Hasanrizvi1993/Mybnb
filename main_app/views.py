from ast import Delete
from audioop import reverse
from re import template
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse, HttpResponseRedirect # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Home, Car
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

@method_decorator(login_required, name='dispatch')
class Home_Create(CreateView):
    model = Home
    fields = ['location', 'home_type', 'amenities', 'image', 'contact_name', 'contact_email', 'bedrooms', 'bathrooms', 'price', 'available']
    template_name = "home_create.html"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/homes')


class Home_Detail(DetailView):
    model = Home
    template_name = "home_detail.html"


@method_decorator(login_required, name='dispatch')
class Home_Update(UpdateView):
    model = Home
    fields = ['location', 'home_type', 'amenities', 'image', 'contact_name', 'contact_email', 'bedrooms', 'bathrooms', 'price', 'available']
    template_name = "home_update.html"
    def get_success_url(self):
        return reverse('home_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class Home_Delete(DeleteView):
    model = Home
    template_name = "home_delete_confirmation.html"
    success_url = "/homes/"


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    homes = Home.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'homes': homes})


#Car Views
def car_home(request):
    cars = Car.objects.all()
    return render(request, 'car_index.html', {'cars': cars})

def car_show(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_show.html', {'car': car})

@method_decorator(login_required, name='dispatch')
class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'image', 'color', 'car_type', 'available']
    template_name = "car_form.html"
    success_url = '/cars'

@method_decorator(login_required, name='dispatch')
class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'image', 'color', 'car_type', 'available']
    template_name = "car_update.html"
    success_url = '/cars'


@method_decorator(login_required, name='dispatch')
class CarDelete(DeleteView):
    model = Car
    template_name = "car_confirm_delete.html"
    success_url = '/cars'







# django auth
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cats')

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: # it was a get request so send the emtpy login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
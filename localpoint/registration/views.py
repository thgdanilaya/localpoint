from django.contrib.auth.views import LoginView
from django.db import connection
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from registration.models import Users
from django.contrib.postgres.search import SearchVector

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

from registration.forms import RegisterUserForm, LoginUserForm


class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy('sign_in')


def home(request):
    return render(request, "registration/home.html")


def profile(request):
    return render(request, "registration/profile.html")


def reg_success(request):
    if request.method == 'POST':
        form_name = RegisterUserForm(request.POST)
        if form_name.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            b = Users(username=username, email=email, password=password)
            b.save()
            return render(request, 'registration/sign_in.html')
        else:
            return render(request, 'registration/sign_up.html', {"form": form_name})

    return HttpResponseNotFound("hello")


def log_success(request):
    if request.method == 'POST':
        form_name = LoginUserForm(request.POST)
        if form_name.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            print(Users.objects.filter(email=email))
            if Users.objects.filter(email=email, password=password):
                return render(request, 'registration/profile.html')
            else:
                return render(request, 'registration/sign_in.html')

    return HttpResponseNotFound("hello")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/sign_in.html'
    success_url = reverse_lazy('profile')

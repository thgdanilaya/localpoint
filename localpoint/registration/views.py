from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render
from registration.models import Users

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

from registration.forms import RegisterUserForm


class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy('home')


def home(request):
    return render(request, "registration/home.html")


def reg_success(request):
    if request.method == 'POST':
        form_name = RegisterUserForm(request.POST)
        if form_name.is_valid():
            username = form_name.cleaned_data.get("Inputusername")
            email = form_name.cleaned_data.get("Inputemail")
            password = form_name.cleaned_data.get("InputPassword")
            print(username, email, password)
            b = Users(username=username, email=email, password=password)
            b.save()
            return render(request, 'registration/home.html')
    return HttpResponseNotFound("hello")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/sign_in.html'
    success_url = reverse_lazy('home')

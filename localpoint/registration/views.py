from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
            from registration.models import Users
            username = form_name.cleaned_data.get("Inputusername")
            email = form_name.cleaned_data.get("Inputemail")
            password = form_name.cleaned_data.get("InputPassword")
            b = Users(username=username, email=email, password=password)
            b.save()


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/sign_in.html'
    success_url = reverse_lazy('home')

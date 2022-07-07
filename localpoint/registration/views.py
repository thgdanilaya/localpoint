from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class Registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/sign_up.html"


def home(request):
    return render(request, "registration/home.html")



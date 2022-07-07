from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def registration(request):
    return render(request, "registration/sign_up.html")


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class Registration(CreateView):
    form_class = UserCreationForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

    def register(self, request):
        email = request.POST['email']



def home(request):
    return render(request, "registration/home.html")

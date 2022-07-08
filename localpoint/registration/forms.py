from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from registration.models import Users


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        username = forms.CharField(label="Inputusername", max_length=255)
        email = forms.EmailField(label="Inputemail", max_length=255)
        password = forms.CharField(label="InputPassword", max_length=255)
        repeat_password = forms.CharField(label="repeatPassword", max_length=255)

        def __str__(self):
            return self.username

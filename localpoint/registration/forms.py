from django import forms

from registration.models import Users


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        username = forms.CharField(max_length=255)
        email = forms.EmailField(max_length=255)
        password = forms.CharField(max_length=255)
        repeat_password = forms.CharField(max_length=255)

        def __str__(self):
            return self.username


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        username = forms.CharField(label="Inputusername", max_length=255)
        email = forms.EmailField(label="Inputemail", max_length=255)
        password = forms.CharField(label="InputPassword", max_length=255)

        def __str__(self):
            return self.username

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'email', 'password1', 'password2']


class Productform(forms.Form):
    product = forms.IntegerField()

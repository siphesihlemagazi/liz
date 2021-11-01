from django.forms import ModelForm, Textarea
from .models import Service
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'address', 'experience', 'phone', 'email']

        widgets = {
            'experience': Textarea,
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

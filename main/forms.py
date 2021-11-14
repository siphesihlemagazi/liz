from django.forms import ModelForm, Textarea
from .models import Service
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'location', 'experience', 'phone', 'email']

        widgets = {
            'experience': Textarea,
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already in use.')

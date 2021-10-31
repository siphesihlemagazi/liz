from django.forms import ModelForm
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'address', 'experience', 'phone', 'email']

import django_filters
from django_filters import CharFilter
from .models import Service


class ServiceFilter(django_filters.FilterSet):
    service_name = CharFilter(lookup_expr='icontains')
    location = CharFilter(lookup_expr='icontains')
    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['experience', 'phone', 'email', 'datecreated', 'author'] 
        # meaning only name & address will be used

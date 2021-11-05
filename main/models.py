from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    experience = models.CharField(max_length=400)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    datecreated = models.DateTimeField(default=datetime.now, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.service_name

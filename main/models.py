from django.db import models
from datetime import datetime


class Service(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    experience = models.CharField(max_length=400)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    datecreated = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

from django.db import models
from hms.models import Person


class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    address = models.CharField(max_length=256, default=None)

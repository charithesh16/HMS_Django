from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    type = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

# class Patient(models.Model):

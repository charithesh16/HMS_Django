from django.db import models
from patient.models import Patient
from hms.models import Person
from datetime import datetime


class Doctor(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    address = models.CharField(max_length=256, default=None)

    def __str__(self):
        return self.person.user.username


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    prescription = models.CharField(max_length=200)
    disease = models.CharField(max_length=256)
    date = models.DateTimeField()

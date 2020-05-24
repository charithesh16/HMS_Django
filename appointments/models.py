from django.db import models
from patient.models import Patient
from doctor.models import Doctor
from hms.models import Receptionist
# Create your models here.
from django.contrib.auth.models import User


class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    receptionist = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    date = models.DateTimeField()
    choices = [("pending", "pending"), ("completed", "completed")]
    status = models.CharField(
        choices=choices, max_length=256, default="pending")

    def __str__(self):
        return self.patient.person.user.username + ' appointment with ' + self.doctor.person.user.username

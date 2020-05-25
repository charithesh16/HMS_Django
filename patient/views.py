from django.shortcuts import render, HttpResponse, redirect
from doctor.models import Prescription
from hms.models import Person
from django.contrib.auth.models import User
from .models import Patient


def medicalhistory(request):
    person = Person.objects.get(user=User.objects.get(username=request.user))
    patient = Patient.objects.get(person=person)
    prescriptions = Prescription.objects.filter(
        patient=patient).order_by('date')
    return render(request, 'patient/medicalhistory.html', {'prescriptions': prescriptions, 'person': person})

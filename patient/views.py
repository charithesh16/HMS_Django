from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Patient
from hms.models import Person


def profile(request):
    user = request.user
    user = User.objects.get(username=user)
    person = Person(user=user)
    if Patient.objects.filter(person=person).exists():
        patient = Patient.objects.filter(person=person)[0]
        return render(request, 'patient/profile.html', {'patient': patient})
    else:
        return render(request, 'patient/profile.html', {'patient': None})

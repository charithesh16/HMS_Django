from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from patient.models import Patient
from .models import Doctor, Prescription
from hms.models import Person


def prescription(request):
    if request.method == "POST":
        patient = request.POST["patient"]
        disease = request.POST["disease"]
        prescription = request.POST["prescription"]
        patient_person = Person.objects.get(
            user=User.objects.get(username=patient))
        doctor_person = Person.objects.get(
            user=User.objects.get(username=request.user))
        pres = Prescription(patient=Patient.objects.get(
            person=patient_person), doctor=Doctor.objects.get(person=doctor_person))
        pres.prescription = prescription
        pres.disease = disease
        pres.save()
        return redirect('prescription')
    else:
        print(request.user)
        person = Person.objects.get(
            user=User.objects.get(username=request.user))
        patients = Patient.objects.all()
        prescriptions = Prescription.objects.filter(
            doctor=Doctor.objects.get(person=person))
        print(prescriptions)
        return render(request, 'doctor/prescription.html', {'prescriptions': prescriptions, 'patients': patients, 'person': person})

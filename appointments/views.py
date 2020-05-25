from django.shortcuts import render
from appointments.models import Appointments
from hms.models import Person
from patient.models import Patient
from doctor.models import Doctor
from django.contrib.auth.models import User
# Create your views here.


def appointment(request):
    person = Person.objects.get(user=User.objects.get(username=request.user))
    if person.type == 1:
        appointments = Appointments.objects.filter(
            patient=Patient.objects.filter(person=person)[0]).order_by('date')
        return render(request, 'appointments.html', {'appointments': appointments, 'person': person})
    if person.type == 0:
        appointments = Appointments.objects.filter(
            doctor=Doctor.objects.filter(person=person)[0]).order_by('date')
        return render(request, 'appointments.html', {'appointments': appointments, 'person': person})

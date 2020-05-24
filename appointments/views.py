from django.shortcuts import render
from appointments.models import Appointments
from hms.models import Person
from patient.models import Patient
# Create your views here.


def appointment(request):
    person = Person.objects.get(user=User.objects.get(username=request.user))
    appointments = Appointments(patient=Patient.objects.filter(person=person))
    return render(request, 'patient/appointments.html', {'appointments': appointments, 'person': person})

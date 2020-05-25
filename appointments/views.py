from django.shortcuts import render, redirect
from appointments.models import Appointments
from hms.models import Person, Receptionist
from patient.models import Patient
from doctor.models import Doctor
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.


def appointment(request):
    person = Person.objects.get(user=User.objects.get(username=request.user))
    if person.type == 1:
        appointments = Appointments.objects.filter(
            patient=Patient.objects.filter(person=person)[0]).order_by('date')
        return render(request, 'appointments.html', {'appointments': appointments, 'person': person})
    elif person.type == 0:
        appointments = Appointments.objects.filter(
            doctor=Doctor.objects.filter(person=person)[0]).order_by('date')
        return render(request, 'appointments.html', {'appointments': appointments, 'person': person})
    else:
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()
        appointments = Appointments.objects.filter(
            receptionist=Receptionist.objects.filter(person=person)[0]).order_by('date')
        return render(request, 'receptionist/appointments.html', {'appointments': appointments, 'person': person, 'patients': patients, 'doctors': doctors})


def create_appointment(request):
    if request.method == 'POST':
        patient = request.POST['patient']
        doctor = request.POST['doctor']
        date_time = request.POST['date'] + 'T' + request.POST['time']
        status = request.POST['status']
        print(date_time)
        date_time = datetime(
            *[int(v) for v in date_time.replace('T', '-').replace(':', '-').split('-')])
        patient_p = Person.objects.get(user=User.objects.get(username=patient))
        doctor_p = Person.objects.get(user=User.objects.get(username=doctor))
        receptionist_p = Person.objects.get(
            user=User.objects.get(username=request.user))
        appoint = Appointments(patient=Patient.objects.get(person=patient_p), doctor=Doctor.objects.get(
            person=doctor_p), receptionist=Receptionist.objects.get(person=receptionist_p))
        appoint.date = date_time
        appoint.status = status

        appoint.save()
        return redirect('appointment')


def updateAppointment(request, appoint_id=None):
    appointment = Appointments.objects.get(id=appoint_id)
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        # id = request.POST["id"]
        doctor = request.POST['doctor']
        date_time = request.POST['date'] + 'T' + request.POST['time']
        status = request.POST['status']
        date_time = datetime(
            *[int(v) for v in date_time.replace('T', '-').replace(':', '-').split('-')])
        appoint = Appointments.objects.get(pk=int(appoint_id))
        person = Person.objects.get(user=User.objects.get(username=doctor))
        doctor_p = Doctor.objects.get(person=person)
        person_rec = Person.objects.get(
            user=User.objects.get(username=request.user))
        receptionist_p = Receptionist.objects.get(person=person_rec)
        appoint.doctor = doctor_p
        appoint.date = date_time
        appoint.status = status
        appoint.receptionist = receptionist_p
        appoint.save()
        return redirect('appointment')
        pass
    return render(request, 'receptionist/update_appointment.html', {'appointment': appointment, 'doctors': doctors})


def delete(request, appoint_id=None):
    appointment = Appointments.objects.get(id=appoint_id)
    appointment.delete()
    return redirect('appointment')

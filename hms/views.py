from django.shortcuts import render, redirect
from .models import Person, Receptionist, Rpatient
from django.contrib.auth.models import User, Group
from django.contrib import auth
from patient.models import Patient
from doctor.models import Doctor


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # person = Person(user=request.user.username)
            # print(Person.objects.get(user=user))
            person = Person.objects.filter(user=user).values('type')[0]
            print(person)
            return redirect('home')
        else:
            # messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'hms/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        personType = request.POST['personType']

        if password == password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request, 'Username has already been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # messages.error(request, 'Email is already in use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    person = Person(user=user)
                    person.type = int(personType)
                    if person.type == 1:
                        p_group = Group.objects.get(name='Patient')
                        p_group.user_set.add(user)
                    else:
                        d_group = Group.objects.get(name='Doctor')
                        d_group.user_set.add(user)
                    person.save()
                    return redirect('login')

        else:
            # messages.error(request, 'passwords do not match')
            return redirect('register')
        return redirect('register')
    else:
        return render(request, 'hms/register.html')


def home(request):
    user = User.objects.get(username=request.user)
    person = Person.objects.get(user=user)
    print("user", person.user.username)
    print("type", person.type)
    return render(request, 'hms/home.html', {'person': person})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request,'You are now logged out')
        return redirect('login')


def profile(request):
    user = request.user
    user = User.objects.get(username=user)
    person = Person.objects.get(user=user)
    if person.type == 1:
        check = Patient.objects.filter(person=person).exists()
        if check:
            x = Patient.objects.filter(person=person)[0]
        else:
            x = Patient()
    else:
        check = Doctor.objects.filter(person=person).exists()
        if check:
            x = Doctor.objects.filter(person=person)[0]
        else:
            x = Doctor()
    if request.method == 'POST':
        phone = request.POST['phone']
        gender = request.POST['gender']
        address = request.POST['address']
        age = request.POST['age']

        if phone and gender and address and age:
            if check:
                # print(x.objects.filter(person=person)[0])
                obj = x
                obj.phone = phone
                obj.address = address
                obj.age = age
                obj.gender = gender
                obj.save()
                return redirect('home')
            else:
                obj = x
                obj.person = person
                obj.phone = phone
                obj.address = address
                obj.age = age
                obj.gender = gender
                obj.save()
                return redirect('home')

        else:

            print("Error Occured: ", phone, gender, address, age)
    else:

        if check:
            x_person = x
            return render(request, 'hms/profile.html', {'x': x_person, 'person': person})
        else:
            return render(request, 'hms/profile.html', {'x': None, 'person': person})


def patients(request):
    user = User.objects.get(username=request.user)
    receptionist = Receptionist.objects.get(
        person=Person.objects.get(user=user))
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        age = request.POST["age"]
        obj = Rpatient(receptionist=receptionist, name=name,
                       phone=phone, email=email, gender=gender, age=age)
        obj.save()

    patients = Rpatient.objects.filter(receptionist=receptionist)
    return render(request, 'receptionist/patients.html', {'patients': patients})


def delete_patient(request, patient_id=None):
    user = User.objects.get(username=request.user)
    receptionist = Receptionist.objects.get(
        person=Person.objects.get(user=user))
    patient = Rpatient.objects.get(id=patient_id)
    patient.delete()
    patients = Rpatient.objects.filter(receptionist=receptionist)
    # return render(request, 'receptionist/patients.html', {'patients': patients})
    return redirect('rpatients')


def update_patient(request, patient_id=None):
    patient = Rpatient.objects.get(id=patient_id)
    print(patient)
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        age = request.POST["age"]
        patient.name = name
        patient.phone = phone
        patient.email = email
        patient.gender = gender
        patient.age = age
        patient.save()
        return redirect('rpatients')
    # patients = Rpatient.objects.filter(receptionist=receptionist)
    return render(request, 'receptionist/update_patient.html', {'patients': patient})


def contact(request):
    user = User.objects.get(username=request.user)
    person = Person.objects.get(user=user)
    return render(request, 'contact.html', {'person': person})


def about(request):
    user = User.objects.get(username=request.user)
    person = Person.objects.get(user=user)
    return render(request, 'about.html', {'person': person})

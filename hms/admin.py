from django.contrib import admin
from .models import Person, Receptionist, Rpatient

# Register your models here.
admin.site.register(Person)
admin.site.register(Receptionist)
admin.site.register(Rpatient)

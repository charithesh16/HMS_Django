from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('p_profile/', views.profile, name="patient_profile"),
]

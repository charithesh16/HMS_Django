from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('patients/', views.patients, name='rpatients'),
    path('patients/<int:patient_id>', views.delete_patient, name='delete_patient'),
    path('update_patient/<int:patient_id>',
         views.update_patient, name='update_patient'),


]

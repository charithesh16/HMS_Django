from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('update/<int:appoint_id>', views.updateAppointment, name='update'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('delete/<int:appoint_id>', views.delete, name="delete"),

]

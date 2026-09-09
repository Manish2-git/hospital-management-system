from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("patients/", views.patient_list, name="patient_list"),
    path("appointments/", views.appointment_list, name="appointment_list"),
    path("emergency-queue/", views.emergency_queue_view, name="emergency_queue"),
]

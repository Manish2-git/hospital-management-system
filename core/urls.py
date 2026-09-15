from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("patients/", views.patient_list, name="patient_list"),
    path("patients/add/", views.patient_add, name="patient_add"),
    path("patients/<int:pk>/edit/", views.patient_edit, name="patient_edit"),
    path("patients/<int:pk>/delete/", views.patient_delete, name="patient_delete"),
    path("appointments/", views.appointment_list, name="appointment_list"),
    path("emergency-queue/", views.emergency_queue_view, name="emergency_queue"),
]

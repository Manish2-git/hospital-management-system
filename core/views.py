from django.http import HttpResponse
from django.shortcuts import render
from  .models import Patient,  Appointment

def home(request):
        return HttpResponse("Welcome to the hospital management system!")

def patient_list(request):
        patients = Patient.objects.all()
        return render(request, "core/patient_list.html", {"patients": patients})

def appointment_list(request):
        appointments = Appointment.objects.all()
        return render(request, "core/appointment_list.html", {"appointments": appointments})
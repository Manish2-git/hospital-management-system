from django.http import HttpResponse
from django.shortcuts import render
from  .models import Patient

def home(request):
        return HttpResponse("Welcome to the hospital management system!")

def patient_list(request):
        patients = Patient.objects.all()
        return render(request, "core/patient_list.html", {"patients": patients})
from django.http import HttpResponse
from django.shortcuts import render
from  .models import Patient,  Appointment
from .emergency_queue import get_prority_queue
from django.shortcuts import redirect
from .forms import PatientForm

def home(request):
        return render(request, "core/home.html")

def patient_list(request):
        patients = Patient.objects.all()
        return render(request, "core/patient_list.html", {"patients": patients})

def appointment_list(request):
        appointments = Appointment.objects.all()
        return render(request, "core/appointment_list.html", {"appointments": appointments})

def emergency_queue_view(request):
        ordered_patients = get_prority_queue()
        return render(request, "core/emergency_queue.html", {"patients": ordered_patients})

def patient_add(request):
        if request.method == "POST":
                form  = PatientForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect("patient_list")
                else:
                        form = PatientForm()
                        return render(request, "core/patient_form.html", {"form": form})

def patient_edit(request, pk):
        patient = Patient.objects.get(id=pk)
        if request.method == "POST":
                form = PatientForm(request.POST, instance=patient)
                if form.is_valid():
                        form.save()
                        return redirect("patient_list")
        else:
                        form = PatientForm(instance=patient)
        return render(request, "core/patient_form.html", {"form": form})               

def patient_delete(request, pk):
        patient = Patient.objects.get(id=pk)
        if  request.method == "POST":
                patient.delete()
                return redirect("patient_list")
        return render(request, "core/patient_confirm_delete.html", {"patient": patient})                



from django.db import models   
SPECIALIZATION_CHOICES = [
        ("general", "General Physician"),
        ("carddiology",  "cardiology"),
        ("neurology", "Neurology"),
]    
class Doctor (models.Model):
        name = models.CharField(max_length=100)
        specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES, default="general")
        phone = models.CharField(max_length=20, blank=True)
        email = models.CharField(blank=True)
        is_available = models.BooleanField(default=True)

GENDER_CHOICES = [
        ("m", "male"),
        ("f", "female"),
]

SEVERITY_CHOICES = [
        (1, "Critical"), 
        (2,  "Serious"), 
        (3, "Mild"),
        (4, "Minor"),
]

class Patient(models.Model):
        name = models.CharField(max_length=100)
        age = models.PositiveIntegerField()
        gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="M")
        phone = models.CharField(max_length=20, blank=True)
        severity = models.IntegerField(choices=SEVERITY_CHOICES, default=3)

class Appointment(models.Model):
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        doctor  = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        date = models.DateField()
        time = models.TimeField()
        reason = models.CharField(max_length=200, blank=True)
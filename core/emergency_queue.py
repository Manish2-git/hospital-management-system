import heapq
from .models import Patient

def get_prority_queue():

    heap = []
    for patient in Patient.objects.all():
        heapq.heappush(heap, (patient.severity, patient.id, patient))

    ordered_patients  =[]
    while  heap:
        severity, pid, patient = heapq.heappop(heap)
        ordered_patients.append(patient)

        return ordered_patients    
from django.shortcuts import render
from .models import AppointmentModel
from .serializers import AppointmentSerializer
from rest_framework import viewsets

# Create your views here.

class AppointmentView(viewsets.ModelViewSet):
    queryset=AppointmentModel.objects.all()
    serializer_class=AppointmentSerializer

    #custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        doctor_id = self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset
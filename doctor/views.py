from django.shortcuts import render
from rest_framework import viewsets
from .models import SpecializationModel,DesignationsModel,AvailableTimeModel,DoctorModel,ReviewModel
from .serializers import SpecializationSerializer,DesignationSerializer,AvailableTimeSerializer,DoctorSerializer,ReviewSerializer

# Create your views here.

class SpecializationView(viewsets.ModelViewSet):
    queryset = SpecializationModel.objects.all()
    serializer_class=SpecializationSerializer

class DesignationView(viewsets.ModelViewSet):
    queryset = DesignationsModel.objects.all()
    serializer_class=DesignationSerializer

class DoctorView(viewsets.ModelViewSet):
    queryset=DoctorModel.objects.all()
    serializer_class=DoctorSerializer

class AvialableTimeView(viewsets.ModelViewSet):
    queryset=AvailableTimeModel.objects.all()
    serializer_class=AvailableTimeSerializer

class ReviewView(viewsets.ModelViewSet):
    queryset=ReviewModel.objects.all()
    serializer_class=ReviewSerializer
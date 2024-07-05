from django.shortcuts import render
from .models import ServiceModel
from .serializers import ServiceSerializers
from rest_framework import viewsets
# Create your views here.


class ServiceView(viewsets.ModelViewSet):
    queryset=ServiceModel.objects.all()
    serializer_class=ServiceSerializers
from django.shortcuts import render
from .serializers import ContactUsSerializers
from .models import ContactUsModel
from rest_framework import viewsets
# Create your views here.


class ContactUsViews(viewsets.ModelViewSet):
    queryset=ContactUsModel.objects.all()
    serializer_class=ContactUsSerializers
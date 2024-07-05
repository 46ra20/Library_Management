from rest_framework import serializers
from .models import ContactUsModel

class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = '__all__'

from rest_framework import serializers
from .models import ServiceModel

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields ='__all__'
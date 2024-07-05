from rest_framework import serializers
from .models import AppointmentModel

class AppointmentSerializer(serializers.ModelSerializer):
    # patient = serializers.StringRelatedField(many=False)
    # time = serializers.StringRelatedField(many=False)
    # doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = AppointmentModel
        fields = '__all__'
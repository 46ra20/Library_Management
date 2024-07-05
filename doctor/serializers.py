from rest_framework import serializers
from .models import SpecializationModel,DesignationsModel,DoctorModel,AvailableTimeModel,ReviewModel

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializationModel
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignationsModel
        fields = '__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTimeModel
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True,read_only=True)
    specialization = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model  = DoctorModel
        fields = '__all__'



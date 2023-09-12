from rest_framework import serializers
from .models import MedicalData

class MedicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalData
        fields = '__all__'
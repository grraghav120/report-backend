from rest_framework import serializers
from .models import HospitalUser

class HospitalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalUser
        fields = '__all__'

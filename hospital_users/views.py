from rest_framework import generics
from .models import HospitalUser
from .serializers import HospitalUserSerializer

class HospitalUserCreateView(generics.CreateAPIView):
    queryset = HospitalUser.objects.all()
    serializer_class = HospitalUserSerializer

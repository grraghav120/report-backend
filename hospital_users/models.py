from django.db import models
from django.contrib.auth.models import User

class HospitalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    gmail = models.EmailField(unique=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField()
    phone = models.BigIntegerField()

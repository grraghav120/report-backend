from django.contrib import admin
from .models import MedicalData

class MedicalDataAdmin(admin.ModelAdmin):
    @staticmethod
    def get_all_fields(obj):
        return [field.name for field in obj._meta.get_fields()]

    list_display = get_all_fields(MedicalData)  # Display all fields in the admin list view
admin.site.register(MedicalData, MedicalDataAdmin)

from django.contrib import admin
from .models import Staff, Appointment, Patient, Department

# Register your models here.
admin.site.register(Staff)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Department)
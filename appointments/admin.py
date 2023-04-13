from django.contrib import admin
from .models import Staff, Appointment, Patient, Department, Address, Facility

# Register your models here.
admin.site.register(Staff)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(Address)
admin.site.register(Facility)
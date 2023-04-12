from django.contrib import admin
from .models import Staff, Appointment, Patient

# Register your models here.
admin.site.register(Staff)
admin.site.register(Patient)
admin.site.register(Appointment)
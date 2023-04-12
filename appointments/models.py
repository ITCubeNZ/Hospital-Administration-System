from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    """
        Model for Appointments 

        Appointment ID: Primary Key
        Patient ID: Foreign Key for Patient Table and should represent their NHI.
        Staff ID: Foreign Key for Staff Table this should be representative of their current staff code.
        Appointment Date: Should represent the date and time the appointment is booked for. 
    """
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20)
    appointment_date = models.DateTimeField()
    contact_phone = models.CharField(max_length=15)


class Patient(models.Model):
    """
        Model for Patients

        patient_id = NHI Number
        first_name = The first name of the patient
        last_name = The last name of the patient
        dob = The Date of Birth of the patient
        phone = This represents the pateients phone number. 
    """
    patient_id = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateTimeField()
    phone = models.CharField(max_length=15)
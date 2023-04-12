from django.db import models
from django.contrib.auth.models import User

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
    dob = models.DateField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        # String Representation
        return "{}. {} {}".format(self.patient_id, self.first_name, self.last_name )

class Staff(models.Model):
    """
        Models for Staff

        staff_id = Staff Code Representing the Primary Key
        first_name =  First Name of the Staff Member
        last_name = Last name of the staff member
        phone = Contact Number of the Staff Member 
        email = Email of the Staff Member
        description = Brief Description of the Staff Member
    """
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        # String representation
        return "{} {}".format(self.first_name, self.last_name)

class Appointment(models.Model):
    """
        Model for Appointments 

        Appointment ID: Primary Key
        Patient ID: Foreign Key for Patient Table and should represent their NHI.
        Staff ID: Foreign Key for Staff Table this should be representative of their current staff code.
        Appointment Date: Should represent the date and time the appointment is booked for. 
    """
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return "Appointment for {} with {}".format(self.patient, self.staff_id)

class Department(models.Model):
    """
        Models for hospital department. 

        department_id = auto_id representing the ID
        department_name = Represents the department_name
        hod = Represents the head of department
    """
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    hod = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        # String Reperesentation
        return "{}".format(self.department_name)


    
from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    """
        Address Model
    """
    address_id = models.AutoField(primary_key=True)
    street_details = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
            String Representation of Address Model
        """
        return "{}, {}, {}, {}".format(self.street_details, self.suburb, self.city, self.zipcode)

class Department(models.Model):
    """
        Models for hospital department. 

        department_id = auto_id representing the ID
        department_name = Represents the department_name
        hod = Represents the head of department
    """
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    no_of_appointment_rooms = models.IntegerField()
    no_of_hospital_beds = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        # String Reperesentation
        return "{}".format(self.department_name)

class Patient(models.Model):
    """
        Model for Patients

        patient_id = NHI Number
        first_name = The first name of the patient
        last_name = The last name of the patient
        dob = The Date of Birth of the patient
        phone = This represents the pateients phone number. 
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    patient_id = models.CharField(max_length=7, primary_key=True, name="NHI")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(name="Date of Birth")
    phone = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

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
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    date_of_birth = models.DateField(name="Date of Birth")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

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
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, name="Staff")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    contact_phone = models.CharField(max_length=15)
    last_updated = models.DateTimeField(auto_now=True)
    by_referral = models.BooleanField(default=False)
    appointment_charges = models.FloatField(default=0.00)

    def __str__(self):
        return "Appointment for {} with {}".format(self.patient, self.staff_id)
    
class Payment(models.Model):
    """
        Model Representing the Payment Class
    """
    payment_id = models.AutoField(primary_key=True)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    amount_paid = models.FloatField()
    cash = models.BooleanField(default=False)
    card = models.BooleanField(default=True)
    payment_date = models.DateTimeField(auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "payment to be paid on {}.".format(self.payment_date)

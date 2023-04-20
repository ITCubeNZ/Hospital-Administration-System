from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from appointments.models import Patient, Appointment, Address

class CreateUserForm(UserCreationForm):
    """
        User Registration Form
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UpdateAccountForm(forms.ModelForm):
    """
        Form To Update the Account
    """
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "Date of Birth", "phone", "address"]

class AppointmentForm(forms.ModelForm):
    """
        Form to Add an Appointment
    """
    class Meta:
        model = Appointment
        fields = ["staff_id", "department", "appointment_date", "contact_phone", "by_referral", "appointment_charges"]

class AddressForm(forms.ModelForm):
    """
        Form used by users to add their address. 
    """
    class Meta:
        model = Address
        fields = "__all__"
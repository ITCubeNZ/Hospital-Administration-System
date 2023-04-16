from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from appointments.models import Patient, Appointment

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
        fields = ['first_name', 'last_name', 'phone']

class AppointmentForm(forms.ModelForm):
    """
        Form to Add an Appointment
    """
    class Meta:
        model = Appointment
        fields = "__all__"

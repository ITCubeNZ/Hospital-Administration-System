from django.shortcuts import render, redirect
from appointments.models import Staff, Department, Address, Patient, Appointment
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UpdateAccountForm, AppointmentForm, AddressForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView

def index(request):
    """
        Returns the HomePage
    """
    
    return render(request, "index.html")

def staff(request):
    """
        Returns a list of Staff Members
    """
    staff = Staff.objects.all()

    return render(request, "staff.html", context={"staff": staff})

def view_staff(request, staff_id):
    """
        Returns a view of details of a staff member
    """
    model = Staff.objects.get(pk=staff_id)

    return render(request, 'view_staff.html', {"staff":model})

def department(request):
    """
        Returns a view of a list of departments
    """
    department = Department.objects.all()

    return render(request, "departments.html", context={"department": department})

def view_department(request, department_id):
    """
        Returns a view of a specific department with IDs
    """
    model = Department.objects.get(pk=department_id)
    address = Address.objects.get(pk=model.address_id)

    return render(request, 'view_department.html', {"department": model, "address": address})

def register(request):
    """
        Views for Registration
    """
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Patient')
            user.groups.add(group)
            Patient.objects.create(
                user=user,
                first_name = user.first_name,
                last_name = user.last_name,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context= {'form' : form}

    return render(request, 'accounts/register.html', context)

def login_page(request):
    """
        Views for login
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else: 
            messages.info(request, 'Username or Password is not valid.')
    context = {}

    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    """
        View to log the user out.
    """
    logout(request)
    messages.success(request, 'You have been successfully logged out.')

    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    """
        View for the Patient Dashboard
    """
    if request.user.is_superuser:
        return redirect('/admin')

    context = {}
    current_user = request.user
    current_patient = Patient.objects.get(user=current_user)
    context['patient'] = current_patient
    appointments = Appointment.objects.filter(patient = Patient.objects.get(user=request.user))
    context['appointments'] = len(appointments)
    context['name'] = current_patient.first_name + ' ' + current_patient.last_name

    return render(request, 'patient_dash.html', context)

@login_required(login_url='login')
def book_appointment(request):
    """
        View for booking an appoiontment
    """

    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            Appointment.objects.create(
                patient = Patient.objects.get(user=request.user),
                staff_id = form.cleaned_data.get('staff_id'),
                department = form.cleaned_data.get('department'),
                appointment_date = form.cleaned_data.get('appointment_date'),
                contact_phone = form.cleaned_data.get('contact_phone'),
                by_referral = form.cleaned_data.get('by_referral'),
                appointment_charges = form.cleaned_data.get('appointment_charges')
            )
            messages.success(request, 'Your appointment was successfully booked. ')
            return redirect('dashboard')
        else:
            messages.info(request, "The data wasn't successfully validated. Please make sure appointment date is formateted in YYYY-MM--DD HH-MM-SS. (E.g. 2006-10-25 14:30:00)")

    context = {"form": form}
        
    return render(request, 'book_appointment.html', context)

@login_required(login_url='login')
def view_appointments(request):
    """
        View for viewing a users appointments
    """
    appointments = Appointment.objects.filter(patient = Patient.objects.get(user=request.user))
    no_appointments = len(appointments)

    context = {"appointments": appointments, "no_appointments": no_appointments}

    return render(request, 'view_appointment.html', context)

@login_required(login_url='login')
def update_account(request):
    """
        View for Updating a users Patient Model
    """

    current_patient = Patient.objects.get(user=request.user)
    form = UpdateAccountForm(instance=current_patient)
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST)
        if form.is_valid():
            current_patient.user = request.user
            current_patient.first_name = form.cleaned_data.get('first_name')
            current_patient.last_name = form.cleaned_data.get('last_name')
            current_patient.date_of_birth = form.cleaned_data.get('date_of_birth')
            current_patient.phone = form.cleaned_data.get('phone')
            current_patient.address = form.cleaned_data.get('addresss')
            current_patient.save()

    return render(request, 'update_user.html', {'form': form})

class DeleteAppointmentView(DeleteView):
    model = Appointment
    success_url = "/dashboard"
    template_name = "confirm_delete.html"

@login_required(login_url='login')
def add_address(request):
    """
        View for adding address.
    """
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            Address.objects.create(
                street_details = form.cleaned_data.get('street_details'),
                suburb = form.cleaned_data.get('suburb'),
                city = form.cleaned_data.get('city'),
                zipcode = form.cleaned_data.get('zipcode')
            )
            messages.success(request, "Successfully added address.")
            return redirect('update account')

    return render(request, 'address.html', {"form": form})


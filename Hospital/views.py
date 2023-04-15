from django.shortcuts import render, redirect
from appointments.models import Staff, Department, Address, Patient
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

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
            return redirect('home')
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

def dashboard(request):
    """
        View for the Patient Dashboard
    """

    context = {}

    return render(request, 'patient_dash.html', context)

def book_appointment(request):
    """
        View for booking an appoiontment
    """

    context = {}

    return render(request, 'book_appointment.html', context)

def view_appointments(request):
    """
        View for viewing a users appointments
    """

    context = {}

    return render(request, 'view_appointment.html', context)


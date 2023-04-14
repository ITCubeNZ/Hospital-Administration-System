from django.shortcuts import render, redirect
from appointments.models import Staff, Department, Address
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
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
    logout(request)
    messages.success(request, 'You have been successfully logged out.')

    return redirect('login')


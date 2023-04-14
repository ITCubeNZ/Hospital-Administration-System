from django.shortcuts import render
from appointments.models import Staff, Department, Address

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


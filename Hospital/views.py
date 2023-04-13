from django.shortcuts import render
from appointments.models import Staff

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
    model = Staff.objects.get(pk=staff_id)

    return render(request, 'view_staff.html', {"staff":model})


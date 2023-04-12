from django.shortcuts import render

def index(request):
    """
        Returns the HomePage
    """
    return render(request, "index.html")

def staff(request):
    """
        Returns a list of Staff Members
    """
    return render(request, "staff.html")
"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, staff, view_staff, department, view_department, register, login_page, logoutUser, dashboard, book_appointment, view_appointments, update_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('staff/', staff, name='staff'),
    path('staff/<int:staff_id>', view_staff, name="view staff"),
    path('departments/', department, name='department'),
    path('departments/<int:department_id>', view_department, name="view department"),
    path('register/', register, name='register'),
    path('login/', login_page, name="login"),
    path('logout/', logoutUser, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/book', book_appointment, name="book appointment"),
    path('dashboard/appointments', view_appointments, name="view appointments"),
    path('dashboard/account/update', update_account, name='update account')
]
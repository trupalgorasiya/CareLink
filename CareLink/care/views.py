from django.shortcuts import render
from django.http import *
import re
# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def admin_login(request):
    return render(request, 'admins/admin_login.html')

def admin_registration(request):
    return render(request, 'admins/admin_registration.html')

def patient_login(request):
    return render(request, 'patients/patient_login.html')

def patient_registration(request):
    return render(request,'patients/patient_registration.html')

def physician_login(request):
    return render(request, 'phys/physician_login.html')

def phys_registration(request):
    return render(request,'phys/phys_registration.html')

def forgotpass(request):
    return render(request, 'forgot_password.html')
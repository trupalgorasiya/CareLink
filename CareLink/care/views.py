from django.shortcuts import render
from django.http import *
import re
# Create your views here.
def home(request):
    return render(request, 'home.html')


def admin_login(request):
    return render(request, 'admin_login.html')

def patient_login(request):
    return render(request, 'patient_login.html')

def physician_login(request):
    return render(request, 'physician_login.html')

def forgotpass(request):
    return render(request, 'forgot_password.html')
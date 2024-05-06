from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

# login for student
@login_required(login_url=settings.STUDENT_LOGIN_URL)

def student_dashboard(request):
    return render(request, 'student/dashboard.html')

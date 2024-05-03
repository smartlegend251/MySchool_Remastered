from django.shortcuts import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import *

# Create your views here.
def student_register(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['userName']
        password = request.POST['password']
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            )
        user.set_password(password)
        user.save() 
        return redirect('/Authentication/student_login')
    return render(request, 'authentication/student/student_register.html')


def staff_register(request):
   
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['userName']
        password = request.POST['password']
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            )
        user.set_password(password)
        user.save() 
        return redirect('/Authentication/staff_login/ ')
    return render(request, "authentication/staff/staff_register.html")
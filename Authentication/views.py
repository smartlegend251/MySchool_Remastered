from django.shortcuts import *
from django.contrib.auth import *
from django.contrib import messages
from .models import User

# Create your views here.

def student_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        

        if User.objects.filter(username = username).exists():
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/Student/dashboard')
            else:
                 messages.error(request, "Incorrect Password, please Try Again!")
            
        else :
            messages.error(request, "Username Does not Exist")
            messages.error(request, "Contact to your Class Admin")
            return redirect('Authentication/student_login/')
    return render(request, 'authentication/student/student_login.html')



def staff_login(request):
    if request.method == "POST":
        pass
    return render(request, 'authentication/staff/staff_login.html')


from django.shortcuts import *
from django.contrib.auth import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def student_logout(requst):
    logout(requst)
    return redirect('/Authentication/student_login')
def staff_logout(request):
    logout(request)
    return redirect('/Authentication/staff_login')
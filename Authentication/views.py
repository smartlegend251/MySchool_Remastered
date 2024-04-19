from django.shortcuts import render

# Create your views here.
def student_login(request):
    if request.method == "POST":
        pass
    return render(request, 'student/student_login.html')

def student_register(request):
    if request.method == "POST":
        pass
    return render(request, 'student/student_register.html')

def staff_login(request):
    if request.method == "POST":
        pass
    return render(request, 'staff/staff_login.html')

def staff_register(request):
    if request.method == "POST":
        pass
    return render(request, 'staff/staff_register.html')
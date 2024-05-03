
from django.urls import path
from .views import *

urlpatterns = [
path('student_application', student_register, name='studentregister' ),
path('staff_application', staff_register, name='staffregister' ),


]

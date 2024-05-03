
from django.urls import path
from .views import *

urlpatterns = [
path('student_login/', student_login, name='student_login'),
path('staff_login/', staff_login, name='staff_login'),

]

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Temp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100,blank=True, null=True)
    lastName = models.CharField(max_length=100,blank=True, null=True)
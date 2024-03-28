from django.db import models
from doctor.models import Doctor
# Create your models here.

class Patient(models.Model):
    name=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)
    status=models.TextField(max_length=15,null=True)

    def __str__(self):
       return self.name

class Appointment(models.Model):
     name=models.TextField(max_length=100,null=True)
     number=models.TextField(max_length=100,null=True)
     time=models.TimeField(max_length=100,null=True)
     date=models.DateField(max_length=100,null=True)
     message=models.TextField(max_length=100,null=True)
     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
     status=models.TextField(max_length=15,null=True)




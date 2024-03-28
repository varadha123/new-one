from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Home(request):
    return render(request,'patient/home.html')

def login(request):
    if request.method=='POST':
        
        email=request.POST['email']
        password=request.POST['password']
        if Patient.objects.filter(email=email,password=password).exists():
            return redirect('patient:booking')
        else:
            return render(request,'patient/login.html',{'msg':'INVALID USER OR EMAIL'})
    return render(request,'patient/login.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        patient= Patient(name=name,email=email,password=password)
        patient.save()
        return redirect('patient:login')
        
    return render(request,'patient/signup.html')


def booking(request):
    doctors=Doctor.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        date=request.POST['date']
        time=request.POST['time']
        message=request.POST['message']
        doctor_id=request.POST['doctor']
        doctor=Doctor.objects.get(id=doctor_id)
        appointment=Appointment(name=name,date=date,time=time,number=number,doctor=doctor,message=message,status='waiting')
        appointment.save()
        return render(request,'patient/booking.html',{'msg':'Your Appointment updation will be added in Booking Status'})
    return render(request,'patient/booking.html',{'doctors':doctors})
   


def booking_status(request):
    patients=Appointment.objects.filter(status='confirmed')
    return render(request,'patient/booking_status.html',{'patients':patients})

    
from django.shortcuts import render,redirect
from .models import *
from patient.models import *
# Create your views here.
def doctor_home(request):
    return render(request,'doctor/doctor_home.html')

def doctor_login(request):
    if request.method=='POST':
        name=request.POST['doc_name']
        password=request.POST['password']
        try:
            doctor = Doctor.objects.get(name=name, password=password)
            request.session['docid'] =doctor.id # Store doctor's id in session
            return redirect('doctor:patientlist')
        except Doctor.DoesNotExist:
            return render(request, 'doctor/doctor_login.html', {'msg': 'Invalid credentials'})
    return render(request,'doctor/doctor_login.html')

def update_status_of_patient(request,patient_id):
    appointment=Appointment.objects.get(id=patient_id)
    # email=appointment.email
    appointment.status='confirmed'
    appointment.save()


def remove_apponitment(request,appointment_id):
    Appointment.objects.get(id=appointment_id).delete()
    return redirect('doctor:patientlist')
   

def patientlist(request):
    doc=Doctor.objects.all()
    doctorid = request.session.get('docid')
    
    appointments = Appointment.objects.filter(doctor=doctorid)
    
        
    return render(request,'doctor/patientlist.html',{'appointments':appointments})



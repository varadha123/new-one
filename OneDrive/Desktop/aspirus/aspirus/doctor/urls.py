from django.urls import path
from .import views
app_name='doctor'
urlpatterns=[
    path('doctor_home/',views.doctor_home,name='doctor_home'),
    path('doctor_login/',views.doctor_login,name='doctor_login'),
    path('patientlist/',views.patientlist,name='patientlist'),
    path('update_status_of_patient/<int:patient_id>',views.update_status_of_patient,name='update_status_of_patient'),
    path('remove_apponitment/<int:appointment_id>',views.remove_apponitment,name='remove_apponitment')
]
from django.urls import path
from .import views
app_name='patient'
urlpatterns=[
    path('',views.Home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('booking/',views.booking,name='booking'),
    path('booking_status/',views.booking_status,name='booking_status')

]

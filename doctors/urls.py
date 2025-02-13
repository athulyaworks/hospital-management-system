from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.create_booking,name='booking'),
    path('viewbook/',views.viewbook,name='viewbook'),
    path('update/<int:id>/',views.updatebook,name='updatebook'),
    path('delete/<int:id>/',views.deletebook,name='deletebook'),
    path('department/',views.dep,name='department'),
    path('doctors/',views.doctors,name='doctors'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    
    
]
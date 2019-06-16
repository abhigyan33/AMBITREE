from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage, name = 'homepage'),
    path('aboutUs',views.aboutUs, name = 'aboutUs'),
    path('contactus/', views.contactus,name ='contactus'),
]

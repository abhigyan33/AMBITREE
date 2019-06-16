from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request,'application_ambitree/homepage.html')

def aboutUs(request):
    return render(request,'application_ambitree/aboutUs.html')

def contactus(request):
    return render(request,'application_ambitree/contactUs.html')

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def Map(request):
    return render(request,'Map.html')

def Technology(request):
    return render(request,'Technology.html')

def Ask(request):
    return render(request,'Ask.html')
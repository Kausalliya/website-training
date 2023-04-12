from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def registration(request):
    return render(request,'registration.html')

def contact(request):
    return render(request,'contact.html')

def placement(request):
    return render(request,'placement.html')



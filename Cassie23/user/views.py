from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
   
    return render(request, 'home.html')

def authenticate(request):
    return render(request, 'authenticate.html')

def login(request):
    if request.method=="POST":
        username=request.POST['email_address']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return render(request, 'dashboard.html')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('authenticate')

def signup(request):
    return render(request, 'signup.html')





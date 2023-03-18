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
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username taken")
            return render(request, 'authenticate.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already taken')
            return redirect('signup')
        else:
            user=User.objects.create_superuser(username=username,email=email,password=password)
            user.save()
            messages.info(request,"User Created Successfully")
            auth.login(request,user)
            return render(request,"dashboard.html")
    else:
        return render(request,"home.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

    






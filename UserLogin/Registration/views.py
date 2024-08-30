from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        username=request.POST["u"]
        email=request.POST["ue"]
        password=request.POST["p"]
        cpassword=request.POST["cp"]
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("register")
            else: 
                User.objects.create_user(username=username,email=email,password=password)
                return redirect("logins")
        else:
            messages.info(request,"Passwords Doesn't match")
            return redirect("register")
    else:
        return render(request,"signUp.html")

def logins(request):
    if request.method=="POST":
        u=request.POST["u"]
        p=request.POST["p"]
        user=auth.authenticate(username=u,password=p)
        if user:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Credential doesn't match")
            return redirect("logins")
    
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return render(request,"index.html")

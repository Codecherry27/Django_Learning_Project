from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render(request,"home.html")

def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password doesn't match")
        else:
            my_user = User.objects.create_user(username=uname,email=email,password=password1)
            my_user.save()
            return redirect('login')
        
    return render(request,"signup.html")

def loginpage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request,username=uname,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Account is disabled")
        else:
            return HttpResponse("Username and password incorrect")
        
    return render(request,"login.html")

def logoutpage(request):
    logout(request)
    return redirect('login')
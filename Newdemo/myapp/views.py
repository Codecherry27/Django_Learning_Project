from django.shortcuts import render , HttpResponse
from datetime import datetime;
from myapp.models import createnew;
from django.contrib import messages
# Create your views here.
def index(request):
    # context ={
    #     'variable1':'this is sent',
    #     'variable2':'This is also sent'
    # }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = createnew(name = name, email = email, phone = phone, desc = desc)
        contact.save()
        messages.success(request, "Thanks for contacting us.")
    return render(request,'contact.html')
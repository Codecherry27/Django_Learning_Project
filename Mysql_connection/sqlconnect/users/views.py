from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def alluser(request):
    return HttpResponse("Retuning all users")

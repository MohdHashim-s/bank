from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
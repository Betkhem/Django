from django.http import request
from django.shortcuts import render

# Create your views here.


def HomePage(request):
    return render(request, 'home.html')

def TopPage(request):
    return render(request, 'top.html')

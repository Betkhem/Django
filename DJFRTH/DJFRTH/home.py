from django.http import HttpResponse
from django.shortcuts import render


def house(request):
    return render(request, 'index.html', )
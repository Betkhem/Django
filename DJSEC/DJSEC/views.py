
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reversed(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1] 
    Len = len(user_text.split())
    print(Len)
    return render(request, 'reversed.html', {'reversedtext': reversed_text, 'usertext': user_text, 'len': Len})
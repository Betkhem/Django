from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def dfs_view(request, *args, **kwargs):
    new_dict = {
        'chars' : ['frst', 'sec', 'thrd', '<h2>Yeah!</h2>']
    }
    return render(request, "dfs.html", new_dict)

def about_view(request, *args, **kwargs):
    my_context = {
        "title":'this is about me',
        'my_number':123,
        "this_is_true":True,
        'my_list':[123, 4242, 12313, 'ABC'],
        "my_html":"<h1>Hello there!</h1>"
    }
    return render(request, "about.html" , my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
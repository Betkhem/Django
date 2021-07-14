from django.shortcuts import render
from .forms import ProductForm, RawProductForm
from .models import base
# Create your views here.

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            base.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form':my_form
    }
    return render(request, 'products/product_create.html', context)

def product_detail_view(request):
    obj = base.objects.get(id=1)
    """context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price  
    }"""
    context = {
        'obj': obj
    }
    return render(request, 'products/product_detail.html', context)

"""def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_create_view(request):
    #print(request.GET)
    #print(request.POST)
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
    context = {}
    return render(request, 'products/product_create.html', context)"""

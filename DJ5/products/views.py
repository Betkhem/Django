from django.shortcuts import render
from .models import Product
from .forms import Product_form, Raw_Product_form
# Create your views here.

def home_page(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
        }
    return render(request, 'home.html', context)

def create_page(request):
    obj = Product_form
    obj2 = Raw_Product_form()
    if request.method == 'POST':
        obj2 = Raw_Product_form(request.POST)
        if obj2.is_valid():
            Product.objects.create(**obj2.cleaned_data)
    context = {
        'object':obj,
        'form':obj2
    }
    return render(request, 'create.html', context)

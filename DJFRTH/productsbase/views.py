from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import base
# Create your views here.

def product_create_view(request):
    initial_data = {
        'title':'my title'
    }
    obj = base.objects.get(id=1)
    form = ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = get_object_or_404(base, id=1)
    obj2 = base.objects.all()
    #try:
    #    obj = base.objects.get(id=my_id)
    #except base.DoesNotExist:
    #    raise Http404
    """context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price  
    }"""
    context = {
        'obj': obj,
        'obj2': obj2,
    }
    return render(request, 'products/product_detail.html', context)

def product_delete_view(request, my_id):
    #obj = get_object_or_404(base,id=my_id)
    try:
        obj = base.objects.get(id=my_id)
    except base.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context={
        'object':obj,
    }
    return render(request, 'products/product_delete.html', context)


"""def product_create_view(request):
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
    return render(request, 'products/product_create.html', context)"""

def product_dfs_view(request, my_id):
    #try:
    #    obj = base.objects.get(id=my_id)
    #except base.DoesNotExist:
    #    raise Http404
    """context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price  
    }"""
    obj = get_object_or_404(base, id=my_id)
    context = {
        'obj': obj,
    }
    return render(request, 'products/product_dfs.html', context)

"""def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)

def product_create_view(request):
    #print(request.GET)
    #print(request.POST)
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
    context = {}
    return render(request, 'products/product_create.html', context)"""

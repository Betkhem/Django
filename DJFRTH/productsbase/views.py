from django.shortcuts import render

from .models import base
# Create your views here.
def product_detail_view(request):
    obj = base.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
        'price': obj.price
        
    }
    return render(request, 'product/detail.html', context)
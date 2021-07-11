from django import forms


from .models import base

class ProductForm(forms.ModelForm):
    class Meta:
        model = base
        fields = [
            'title',
            'description',
            'price'
        ]
from django import forms
from django.forms.widgets import Input, Textarea


from .models import base

class ProductForm(forms.ModelForm):
    class Meta:
        model = base
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Yor title'
    }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder':'Yor description',
            'rows':2,
            'cols':22
        }
    ))
    price = forms.DecimalField(initial=9.99)
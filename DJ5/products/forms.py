from django import forms
from django.db.models.fields import Field
from django.forms.forms import Form
from .models import Product

class Product_form(forms.ModelForm):
    class Meta():
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class Raw_Product_form(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your title'
        }))
    description = forms.CharField(max_length=350, widget=forms.Textarea(attrs={
            'placeholder':'Your description',
            'cols':20,
            'rows':10
        }))
    price = forms.DecimalField()

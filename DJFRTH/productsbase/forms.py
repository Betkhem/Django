from django import forms
from django.forms.widgets import Input, Textarea
from .models import base


class ProductForm(forms.ModelForm):
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
    class Meta:
        model = base
        fields = [
            'title',
            'description',
            'price'
        ]
    def cleaned_title(self,*args, **kwargs):
        title = self.cleaned_data.get("title")
        if not 'CFE' in title:
            raise forms.ValidationError('this title is not valid')
        return title
            
        


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
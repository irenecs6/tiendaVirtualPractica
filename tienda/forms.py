from django import forms
from django.forms import ModelForm

from .models import Compra

# class CompraForm (forms.Form):
#     unidades = forms.IntegerField(min_value=1)
    
def CompraForm(ModelForm):
    class meta():
        model = Compra
        fields = ['unidades']
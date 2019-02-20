from django import forms
from django.forms import TextInput, Textarea

from .models import *

class ProductoForm(forms.ModelForm):

    #pro= forms.CharField(label=#"producto", max_length=50)
    class Meta:
        model= Producto
        fields= ("nombre", "marca", "tipo", "precio")
        widgets={
             "nombre": TextInput(attrs= {"class":"class_1"})
         }
from django import forms
from django.forms import TextInput, Textarea

from .models import Producto,Marca

class ProductoForm(forms.ModelForm):

    #pro= forms.CharField(label=#"producto", max_length=50)
    class Meta:
        model= Producto
        fields= ("nombre", "marca", "tipo", "precio")
        widgets={
            "nombre": TextInput(attrs= {"class":"class_1"})
        }


class MarcaForm(forms.ModelForm):

    class Meta:
        model= Marca
        fields= '__all__'
        widgets= {
            "marca_nombre": TextInput(attrs={"class":"class_1"})
        }

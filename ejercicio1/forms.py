from django import forms
from django.forms import TextInput, Textarea

from .models import *

class NumeroForm(forms.ModelForm):

    #pro= forms.CharField(label=#"producto", max_length=50)
    class Meta:
        model = Numero
        fields = ("numero1", "numero2", "numero3")
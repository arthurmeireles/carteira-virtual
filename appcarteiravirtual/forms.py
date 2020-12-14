from django import forms
from django.forms import ModelForm

from . models import *

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
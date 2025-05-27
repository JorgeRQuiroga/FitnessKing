from django import forms
from crudCompleto.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"
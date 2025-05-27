from django import forms
from crudCompleto.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
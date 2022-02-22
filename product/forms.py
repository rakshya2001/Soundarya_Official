from django import forms
from django.contrib.auth.models import User
from . import models
from product.models import Product


class ProductForm(forms.ModelForm):
   class Meta:
    model = Product
    fields = ("__all__")



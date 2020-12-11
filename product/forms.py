from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title",
                  "image",
                  "description",
                  "price", "table",
                  "special_model"]
        widgets = {
            "title": forms.TextInput(attrs={'class': "form-control"}),
            "description": forms.Textarea(attrs={'class': "form-control"}),
            "table": forms.Textarea(attrs={'class': "form-control"}),
            "special_model": forms.Textarea(attrs={'class': "form-control"}),
            "image": forms.Textarea(attrs={'class': "form-control"}),
            "price": forms.NumberInput(attrs={'class':'form-control'})

        }

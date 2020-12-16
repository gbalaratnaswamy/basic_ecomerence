from django import forms
from .models import OrderedItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderedItem
        fields = ["payment_method"]

from django.db import models
from django.contrib.auth.models import User
from product.models import Product

payment_methods = (('CARD', 'CARD'),
                   ('INBK', 'INTERNET BANKING'),
                   ('COD', 'COD'))


# Create your models here.
class OrderedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    no_of_items = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=payment_methods, default='CARD')
    is_payment_complete = models.BooleanField(default=False)


class OrderSet(models.Model):
    order_items = models.ManyToManyField(OrderedItem)
    time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=payment_methods, default='CARD')
    is_payment_complete = models.BooleanField(default=False)

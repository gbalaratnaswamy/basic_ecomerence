from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.
class OrderedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    no_of_items = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

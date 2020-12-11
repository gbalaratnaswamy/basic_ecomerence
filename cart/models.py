from django.db import models

from django.contrib.auth.models import User
from product.models import Product


# Create your models here.
class CartItem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.JSONField(null=True, blank=True)
    products = models.ManyToManyField(Product)

    @staticmethod
    def get_or_create(query_user):
        try:
            cart = CartItem.objects.get(user=query_user)
        except CartItem.DoesNotExist:
            cart = CartItem(user=query_user)
            cart.save()
        return cart

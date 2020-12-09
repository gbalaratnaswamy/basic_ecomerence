from django.db import models
from product.models import Product
from django.contrib.auth.models import User


# Create your models here.
class ProductReview(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,related_name="reviews")
    user = models.OneToOneField(User, on_delete=models.SET_NULL,related_name="reviews_given",null=True)
    rating = models.SmallIntegerField()
    review = models.TextField(max_length=200)

from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.JSONField()
    description = models.TextField(max_length=10000)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    table = models.JSONField(null=True, blank=True)
    special_model = models.TextField(null=True, blank=True)
    stock = models.IntegerField(default=10)
    rating_5 = models.IntegerField(default=0)
    rating_4 = models.IntegerField(default=0)
    rating_3 = models.IntegerField(default=0)
    rating_2 = models.IntegerField(default=0)
    rating_1 = models.IntegerField(default=0)
    rating_avg = models.IntegerField(default=0)

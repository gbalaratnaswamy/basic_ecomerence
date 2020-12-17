from django.contrib import admin
from .models import OrderedItem, OrderSet

# Register your models here.
admin.site.register(OrderedItem)

admin.site.register(OrderSet)

from django.urls import path

from .views import *

urlpatterns = [
    path('product/<p_id>', product_view),
    path('product/<p_id>/add', product_add),
    path("product/create", create_product),
    path("",home)
]

from django.urls import path

from .views import *

urlpatterns = [
    path("product/create", create_product),
    path('product/view/<p_id>', product_view),
    path('product/view/<p_id>/add', product_add),
    path("", home),
    path("product/change/<p_id>", change_product),
    path("test", test),
    path("product/delete/<p_id>", delete_product),
]

from django.urls import path

from .views import *

urlpatterns = [
    path("cart", cart_view),
    path("cart/add/<p_id>", cart_increase),
    path("cart/dec/<p_id>", cart_decrease),
    path("cart/del/<p_id>", cart_delete),
]

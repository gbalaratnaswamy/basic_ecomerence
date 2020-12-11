from django.urls import path

from .views import *

urlpatterns = [
    path("payment", start_payment),
    path("checkout",checkout)
]

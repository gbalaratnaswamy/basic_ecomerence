from django.urls import path

from .views import *

urlpatterns = [
    path("orders", orders_view),

]

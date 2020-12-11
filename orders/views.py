from django.shortcuts import render,redirect
from .models import OrderedItem


# Create your views here.
def orders_view(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    orders = OrderedItem.objects.filter(user=request.user)
    return render(request, "orders.html", {"orders": orders})

from django.shortcuts import render,redirect
from .models import CartItem
# Create your views here.
def cart_view(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request,"cart.html",{"cart":CartItem.objects.filter(user=request.user)})
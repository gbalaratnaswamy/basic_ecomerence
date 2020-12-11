from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from cart.models import CartItem
from orders.models import OrderedItem


# Create your views here.
def start_payment(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    cart = CartItem.objects.get(user=request.user)
    return render(request, "payment.html", {"cart": cart})


def checkout(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    cart = CartItem.objects.get(user=request.user)
    all_products = cart.products.all()
    if len(all_products) == 0:
        return HttpResponse("No items in your cart")
    for product in cart.products.all():
        no_of_items = cart.items[f"{product.id}"]
        order = OrderedItem(user=request.user, product=product, no_of_items=no_of_items,
                            cost=no_of_items * product.price)
        order.save()
    cart.items = {}
    cart.products.clear()
    cart.save()
    return HttpResponse("success")

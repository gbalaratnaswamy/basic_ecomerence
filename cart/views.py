from django.shortcuts import render, redirect, HttpResponse
from .models import CartItem


# Create your views here.
def cart_view(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    try:
        cart = CartItem.objects.get(user=request.user)
    except CartItem.DoesNotExist:
        cart = CartItem(user=request.user)
        cart.save()
    return render(request, "cart.html", {"cart": cart})


def cart_increase(request, p_id):
    cart = CartItem.objects.get(user=request.user)
    try:
        if cart.items[p_id] >= cart.products.get(pk=p_id).stock:
            return HttpResponse("limited stock")
        cart.items[p_id] += 1
        cart.save()
        return HttpResponse(cart.items[p_id])
    except KeyError:
        return HttpResponse("failed")


def cart_decrease(request, p_id):
    cart = CartItem.objects.get(user=request.user)
    try:
        cart.items[p_id] -= 1
        cart.save()
        if cart.items[p_id] == 0:
            cart.products.remove(p_id)
            cart.items.pop(p_id)
            cart.save()
            return HttpResponse(0)
        return HttpResponse(cart.items[p_id])
    except KeyError:
        return HttpResponse("failed")


def cart_delete(request, p_id):
    cart = CartItem.objects.get(user=request.user)
    try:
        cart.items.pop(p_id)
        cart.products.remove(p_id)
        cart.save()
        return HttpResponse("success")
    except KeyError:
        return HttpResponse("failed")

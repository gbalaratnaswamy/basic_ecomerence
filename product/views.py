from django.shortcuts import render, redirect, HttpResponse
from product.models import Product
from .forms import ProductForm
from cart.models import CartItem

from django.contrib.auth.models import User


# Create your views here.
def product_view(request, p_id):
    temp = Product.objects.get(pk=p_id)
    return render(request, "product_template.html",
                  {"product": temp})


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect(f"http://127.0.0.1:8000/test/{form.id}")
    return render(request, "create_product.html", {"form": form})


def product_add(request, p_id):
    try:
        cart = CartItem.objects.get(user=request.user)
    except CartItem.DoesNotExist:
        cart = CartItem(user=request.user)
        cart.save()
    try:
        if p_id not in cart.items:
            cart.items.update({p_id: 1})
            cart.products.add(p_id)
            cart.save()
    except TypeError:
        cart.items = {p_id: 1}
        cart.products.add(p_id)
        cart.save()
    return HttpResponse("added")


def change_product_title(request):
    pass


def change_product_description(request):
    pass


def change_product_price(request):
    pass


def change_product_table(request):
    pass


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

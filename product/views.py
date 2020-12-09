from django.shortcuts import render, redirect, HttpResponse
from product.models import Product
from .forms import ProductForm
from cart.models import CartItem
from reviews.forms import ReviewForm
from django.contrib.auth.models import User
import math


# Create your views here.
def product_view(request, p_id):
    temp = Product.objects.get(pk=p_id)
    form = ReviewForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = temp
            print(type(form.rating))
            if form.rating == 1:
                temp.rating_1 += 1
            elif form.rating == 2:
                temp.rating_2 += 1
            elif form.rating == 3:
                temp.rating_3 += 1
            elif form.rating == 4:
                temp.rating_4 += 1
            elif form.rating == 5:
                temp.rating_5 += 1

            temp.rating_avg = round(((temp.rating_1 + 2 * temp.rating_2 + 3 * temp.rating_3 + 4 * temp.rating_4 +
                                      5 * temp.rating_5) / (temp.rating_1 + temp.rating_2 + temp.rating_3 +
                                                            temp.rating_4 + temp.rating_5)), 2)
            form.save()
            temp.save()
            form = ReviewForm()
    return render(request, "product_template.html",
                  {"product": temp, "form": form})


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect(f"http://127.0.0.1:8000/test/{form.id}")
    return render(request, "create_product.html")


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


def change_product(request, p_id):
    if not request.user.is_authenticated:
        return redirect("/login")
    product = Product.objects.get(pk=p_id)
    product_user = product.user
    if product_user.username == request.user.username:
        form = ProductForm(request.POST or None, instance=product)
        if request.method == "POST":
            if form.is_valid():
                form.save()
        return render(request, "product_edit.html", {"form": form})
    return HttpResponse("access denied")


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

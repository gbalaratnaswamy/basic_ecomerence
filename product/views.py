from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from product.models import Product
from .forms import ProductForm
from cart.models import CartItem
from reviews.forms import ReviewForm
from reviews.models import ProductReview
from django.contrib.auth.models import User
from orders.models import OrderedItem
from django.conf import settings
from django.core.mail import send_mail
import math


# Create your views here.
def product_view(request, p_id):
    try:
        temp = Product.objects.get(pk=p_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if not temp.is_active:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    form = ReviewForm(request.POST or None)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/login")
        if form.is_valid():
            try:
                OrderedItem.objects.get(user=request.user, product=temp)
            except OrderedItem.DoesNotExist:
                return HttpResponseNotAllowed("you have not ordered item please order it to review")
            except OrderedItem.MultipleObjectsReturned:
                pass
            review_given = True
            try:
                ProductReview.objects.get(user=request.user, product=temp)
            except ProductReview.DoesNotExist:
                review_given = False
            except ProductReview.MultipleObjectsReturned:
                pass
            if review_given:
                return HttpResponseNotAllowed("you have already submited review")
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
    product_user = temp.user
    is_seller = product_user.username == request.user.username
    return render(request, "product_template.html",
                  {"product": temp, "form": form, "is_seller": is_seller})


def create_product(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect(f"/product/view/{form.id}")
    else:
        if request.method == "POST":
            print(request.POST['image'])
        print(form.errors)
    return render(request, "create_product.html", {"form": form})


def product_add(request, p_id):
    if not request.user.is_authenticated:
        return redirect("/login")
    cart = CartItem.get_or_create(request.user)
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


def delete_product(request, p_id):
    if request.method == "GET":
        return HttpResponseNotAllowed("Request not allowed")
    if not request.user.is_authenticated:
        return redirect("/login")
    product = Product.objects.get(pk=p_id)
    product_user = product.user
    if product_user.username == request.user.username:
        product.is_active = False
        product.save()
        for item in product.cartitem_set.all():
            item.products.remove(product)
            item.items.pop(product.id)
            item.save()
        return HttpResponse("deleted successfully")
    return HttpResponseNotAllowed("access denied")


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
    return HttpResponseNotAllowed("access denied")


def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "home.html", {"products": products})


def test(request):
    # user = request.user
    # subject = 'welcome to GFG world'
    # message = f'Hi {user.username}, thank you.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [user.email, ]
    # send_mail(subject, message, email_from, recipient_list)
    # return HttpResponse("success")
    cart = CartItem.objects.get(user=request.user)
    return render(request, 'emails/order_complete.html',
                  {"username": 'gbala', 'cart': cart, "total_cost": 100, "total_items": 10})

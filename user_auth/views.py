from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from cart.models import CartItem


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        user = authenticate(username=request.POST["userName"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("/")
        return render(request, "login.html", {"error": "invalid login"})
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/login")


def signup_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        user = User.objects.create_user(request.POST['userName'], request.POST['email'], request.POST['password'])
        user.save()
        cart = CartItem(user=user, items={})
        cart.save()
        login(request, user)
        return redirect("/")
    return render(request, "signup.html")


def home(request):
    return render(request, "home.html")


def user_page(request):
    if request.user.is_authenticated:
        user = User.objects.filter(username=request.user).first()
        return render(request, "user_page.html", {"user": user})
    return redirect("/")
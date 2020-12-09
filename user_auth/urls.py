from django.urls import path

from .views import *

urlpatterns = [
    path("login", login_user),
    path("logout", logout_user),
    path("signup", signup_user),
    path("user", user_page),
    path("user/update/email",update_user_email),
    path("user/update/password",update_user_password)
]

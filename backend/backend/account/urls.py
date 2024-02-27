from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from .views import SignUpView


urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", views.loginView, name="login"),
    path("logout", views.LogOutView, name="logout"),
]
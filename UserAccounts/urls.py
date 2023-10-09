from django.urls import path
from . import views

app_name = "UserAccounts"

urlpatterns = [
    path("login", views.loginUser, name="LoginUser"),
    path("signup", views.signUpUser, name="SignUpUser"),
    path("logout", views.logoutUser, name="LogoutUser")
]

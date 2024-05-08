from django.urls import path  # path nos permite crear las urls que necesitemos
from . import views  # me traigo todas las vistas

app_name = "namespacefirebase"

urlpatterns = [
    path("", views.sign, name="sign"),
    path("signIn/", views.signIn, name="signIn"),
    path("signUp/", views.signUp, name="signUp"),
    path("signUp_register/", views.signUp_register, name="signUp_register"),
    path("logout/", views.logout, name="logout"),
]

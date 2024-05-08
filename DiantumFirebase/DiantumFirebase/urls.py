from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("firebase/", include("firebase.urls", namespace="main-firebase")),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shops", views.getShops, name="getShops"),
    path("products", views.getProducts, name="getProducts"),
]
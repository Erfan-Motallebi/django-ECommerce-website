from django.urls import path

from cart import views



urlpatterns = [
    path("", view=views.cart, name="cart"),
]

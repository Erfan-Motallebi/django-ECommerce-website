from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from store.models import Product


def home(request: HttpRequest) -> HttpResponse:
    all_products = Product.objects.all().filter(is_available=True)
    context = {'products': all_products}
    return render(request, "home.html", context)

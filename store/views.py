from itertools import product

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from category.models import Category
from store.models import Product


# Create your views here.
def store(request: HttpRequest, category_slug: str = None) -> HttpResponse:
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request=request, template_name="store/store.html", context=context)


def product_detail(request: HttpRequest, category_slug: str, product_slug: str) -> HttpResponse:
    single_product = get_object_or_404(Product, slug=product_slug, category__slug=category_slug, is_available=True)
    context = {
        'product': single_product,
    }
    return render(request=request, template_name="store/product_detail.html", context=context)
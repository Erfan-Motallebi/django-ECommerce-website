from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from cart.models import Cart, CartItem
from cart.views import _cart
from category.models import Category
from store.models import Product


# Create your views here.
def store(request: HttpRequest, category_slug: str = None) -> HttpResponse:
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-created_date')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request=request, template_name="store/store.html", context=context)


def product_detail(request: HttpRequest, category_slug: str, product_slug: str) -> HttpResponse:
    single_product = get_object_or_404(Product, slug=product_slug, category__slug=category_slug, is_available=True)
    cart_id = get_object_or_404(Cart, cart_id=_cart(request))
    product = get_object_or_404(Product, pk=single_product.id)
    in_cart = CartItem.objects.filter(cart=cart_id, product=product).exists()
    context = {
        'product': single_product,
        'in_cart': in_cart,
    }
    print(context)
    return render(request=request, template_name="store/product_detail.html", context=context)


def search(request: HttpRequest) -> HttpResponse:
    products = {}
    product_count = 0

    if request.GET["keyword"]:
        keyword = request.GET["keyword"]
        products = Product.objects.filter(Q(product_name__icontains=keyword) | Q(description__icontains=keyword))
    else:
        products = Product.objects.all().filter(is_available=True)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request=request, template_name="store/store.html", context=context)

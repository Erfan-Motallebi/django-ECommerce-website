from django.http import HttpRequest

from cart.models import Cart, CartItem
from cart.views import _cart


def counter(request: HttpRequest) -> dict[str, int] | dict:
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart(request=request))
            cart_items = CartItem.objects.filter(cart=cart)
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)

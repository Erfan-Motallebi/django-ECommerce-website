from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from cart.models import Cart, CartItem
from store.models import Product


def cart(request: HttpRequest, quantity=0, total=0, cart_item=None):
    cart_items = CartItem.objects.filter(cart__cart_id=request.session.session_key)
    for cart_item in cart_items:
        total += cart_item.quantity * cart_item.product.price
        quantity += cart_item.quantity

    tax_price = 2 * total / 100
    grand_total = total
    context = {
        'cart_items': cart_items,
        'quantity': quantity,
        'total': total,
        'tax_price': tax_price,
        'grand_total': grand_total,
    }
    return render(request=request, template_name="store/cart.html", context=context)


def _cart(request: HttpRequest) -> str:
    cart_in_session = request.session.session_key
    if not cart_in_session:
        cart_in_session = request.session.create()
    return cart_in_session


def add_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    product = get_object_or_404(Product, pk=product_id, is_available=True)

    try:
        # Make a new cart id for each product being added to the user cart
        new_cart_id = Cart.objects.get(cart_id=_cart(request))
    except Cart.DoesNotExist:
        new_cart_id = Cart.objects.create(
            cart_id=_cart(request),
        )
        new_cart_id.save()

    # Adding THE new cart [ with new cart id] added to the cart items of the user
    try:
        cart_item = CartItem.objects.get(cart=new_cart_id, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart=new_cart_id,
            product=product,
            quantity=1,
        )
        cart_item.save()
    return redirect('cart')


def remove_cart(request: HttpRequest, product_id: int):
    product = get_object_or_404(Product, pk=product_id)
    cart_id = get_object_or_404(Cart, cart_id=_cart(request))
    cart_item = get_object_or_404(CartItem, cart=cart_id, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request: HttpRequest, product_id: int) -> HttpResponse:
    product = get_object_or_404(Product, pk=product_id)
    cart_id = get_object_or_404(Cart, cart_id=_cart(request))
    cart_item = get_object_or_404(CartItem, cart=cart_id, product=product)
    cart_item.delete()
    return redirect('cart')

from django.contrib import admin

from cart.models import Cart, CartItem

# Register your models here.
admin.site.register(Cart)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ["product", "cart", "quantity", "is_active"]


admin.site.register(
    CartItem,
    CartItemAdmin,
)

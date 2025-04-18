from decimal import Decimal

from django.db import models

from store.models import Product


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product

    def total_price(self) -> Decimal:
        return self.quantity * self.product.price

    def tax_price(self) -> Decimal:
        return self.total_price() + 10

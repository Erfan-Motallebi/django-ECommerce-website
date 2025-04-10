from django.contrib import admin

from store.models import Product, Variations


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "category", "stock", "price", "is_available"]
    prepopulated_fields = {"slug": ("product_name",)}


admin.site.register(Product, ProductAdmin)


class VariationsAdmin(admin.ModelAdmin):
    list_display = ["product", "variation_category", "variation_name", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["product", "variation_category", "variation_name"]


admin.site.register(Variations, VariationsAdmin)

from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.store, name='store'),
    path('category/<slug:category_slug>/', view=views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', view=views.product_detail, name='product_detail'),
    path('search/', view=views.search, name='search'),
]

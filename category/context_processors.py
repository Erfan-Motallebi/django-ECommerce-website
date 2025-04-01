from django.http import HttpRequest

from category.models import Category


def categories(request: HttpRequest) -> dict:
    all_categories = Category.objects.all()
    return dict(categories = all_categories)
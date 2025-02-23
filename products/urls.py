from django.urls import path
from .views import productsView

urlpatterns = [
    path("products/", productsView),
]
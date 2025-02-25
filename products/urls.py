from django.urls import path
from .views import PublisherListView

urlpatterns = [
    path("products/", PublisherListView.as_view(), name="list_products"),
]
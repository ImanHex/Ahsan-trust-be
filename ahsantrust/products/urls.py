from django.urls import path
from .views import ProductView, ProductsListView, ProductsDetailView

urlpatterns = [
    path("products/add", ProductView.as_view(), name="product-add-view"),
    path("products/", ProductsListView.as_view(), name="products-list-view"),
    path("products/<int:pk>", ProductsDetailView.as_view(), name="products-detail-view"),
]

from django.urls import path
from .views import NewsView, NewsListView, NewsDetailView

urlpatterns = [
    path("add", NewsView.as_view(), name="stores-view"),
    path("", NewsListView.as_view(), name="stores-list-view"),
    path("/<int:pk>", NewsDetailView.as_view(), name="stores-detail-view"),
]

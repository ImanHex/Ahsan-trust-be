from django.urls import path
from .views import StoreView, StoresListView, StoresDetailView

urlpatterns = [
    path("stores/add", StoreView.as_view(), name="stores-view"),
    path("stores", StoresListView.as_view(), name="stores-list-view"),
    path("stores/<int:pk>/", StoresDetailView.as_view(), name="stores-detail-view"),
]

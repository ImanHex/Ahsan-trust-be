from django.urls import path
from .views import AnnounceListView, AnnounceDetailView, AnnounceDeleteView

urlpatterns = [
    path("", AnnounceListView.as_view(), name="announce-list"),  # List all announcements
    path("<int:pk>/", AnnounceDetailView.as_view(), name="announce-detail"),  # Retrieve a specific announcement
    path("<int:pk>/delete/", AnnounceDeleteView.as_view(), name="announce-delete"),  # Delete a specific announcement
]

from rest_framework import generics
from .models import announce
from .serializer import AnnounceSerializer

class AnnounceDetailView(generics.RetrieveAPIView):
    queryset = announce.objects.all()
    serializer_class = AnnounceSerializer

class AnnounceDeleteView(generics.DestroyAPIView):
    queryset = announce.objects.all()
    serializer_class = AnnounceSerializer

class AnnounceListView(generics.ListAPIView):
    queryset = announce.objects.all()
    serializer_class = AnnounceSerializer
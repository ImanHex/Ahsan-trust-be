from .serializer import StoresSerializer
from rest_framework import generics
from .models import stores


# Create your views here.
class StoreView(generics.CreateAPIView):
    queryset = stores.objects.all()
    serializer_class = StoresSerializer

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name=name)
        return self.queryset.filter(name=name)


class StoresListView(generics.ListAPIView):
    queryset = stores.objects.all()
    serializer_class = StoresSerializer


class StoresDetailView(generics.RetrieveAPIView):
    queryset = stores.objects.all()
    serializer_class = StoresSerializer

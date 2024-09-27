from .serializer import ProductsSerializer
from rest_framework import generics
from .models import Product


# Create your views here.
class ProductView(generics.CreateAPIView):
    queryset = Product.objects.all().prefetch_related('images')
    serializer_class = ProductsSerializer

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name=name)
        return self.queryset.filter(name=name)


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all().prefetch_related('images')
    serializer_class = ProductsSerializer


class ProductsDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all().prefetch_related('images')
    serializer_class = ProductsSerializer

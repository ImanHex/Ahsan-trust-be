from django.shortcuts import render
from .serializer import NewSerializer
from rest_framework import generics
from .models import news


# Create your views here.


class NewsView(generics.CreateAPIView):
    queryset = news.objects.all()
    serializer_class = NewSerializer

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name=name)
        return self.queryset.filter(name=name)


class NewsListView(generics.ListAPIView):
    queryset = news.objects.all()
    serializer_class = NewSerializer


class NewsDetailView(generics.RetrieveAPIView):
    queryset = news.objects.all()
    serializer_class = NewSerializer

from .models import Store
from rest_framework import serializers
from products.serializer import ProductsSerializer

class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

    products = ProductsSerializer(many=True, read_only=True)


from .models import Store
from rest_framework import serializers


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

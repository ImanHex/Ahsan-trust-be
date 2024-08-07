from .models import stores
from rest_framework import serializers


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = stores
        fields = "__all__"

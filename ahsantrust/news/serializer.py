from .models import news
from rest_framework import serializers


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = "__all__"

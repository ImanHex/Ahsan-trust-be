from datetime import datetime

from rest_framework import serializers
from .models import announce

class AnnounceSerializer(serializers.ModelSerializer):
    class Meta:
        model = announce
        fields = ['title', 'description', 'date', 'time', 'location']

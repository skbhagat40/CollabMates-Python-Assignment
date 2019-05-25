from rest_framework import serializers
from .models import VideoData


class VideoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoData
        fields = '__all__'

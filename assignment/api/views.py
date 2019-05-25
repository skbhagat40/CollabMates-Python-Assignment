import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os
from django.contrib.auth.decorators import user_passes_test
from .paginators import StandardResultsSetPagination
from rest_framework import generics, permissions

from .models import VideoData
from .serializers import VideoDataSerializer

from django.conf import settings

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


# Create your views here.
def index(request):
    return HttpResponse("Hello World! " + settings.BASE_DIR)


@user_passes_test(lambda x: x.is_authenticated and x.is_superuser)
def youtube_data(request):
    r = requests.get(
        'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&order=date&publishedAfter=2013-01'
        '-01T00%3A00%3A00Z&q=ipl&relevanceLanguage=en&safeSearch=strict&topicId=video&key=' + settings.YOUTUBE_KEY)
    j_data = r.json()
    search_result = j_data['items']
    global_data = []
    for res in search_result:
        data_dict = {'video_id': res['id']['videoId'], 'publish_date': res['snippet']['publishedAt'],
                     'title': res['snippet']['title'], 'description': res['snippet']['description'],
                     'thumbnail_url': res['snippet']['thumbnails']['default']['url']}
        global_data.append(data_dict)
    unique_videos = []
    for d in global_data:
        key = d['video_id']
        try:
            _ = VideoData.objects.get(video_id=key)
        except:
            unique_videos.append(d)
    for video in unique_videos:
        serializer = VideoDataSerializer(data=video)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
    serializer = VideoDataSerializer(VideoData.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)


class VideosList(generics.ListAPIView):
    serializer_class = VideoDataSerializer
    queryset = VideoData.objects.order_by('-publish_date')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

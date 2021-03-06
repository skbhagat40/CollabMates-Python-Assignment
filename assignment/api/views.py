import time
import requests
from django.http import HttpResponse, JsonResponse
from .paginators import StandardResultsSetPagination
from rest_framework import generics, permissions
import threading
from .models import VideoData
from .serializers import VideoDataSerializer
from django.conf import settings


def index(request):
    return HttpResponse("Hello World!")

def start_new_thread(function):
    def decorator(*args, **kwargs):
        t = threading.Thread(target = function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator

@start_new_thread
def youtube_data():
    ''' makes call to the youtube search api and saves the data to the database.
        Input Parametres : f_stop - Threading Event
        Output : None
        YouTube API -
        query = ipl
        result type = videos
    '''
    while True:
        print('i am called')
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
                _ = VideoData.objects.filter(video_id=key)
                if len(_) == 0:
                    unique_videos.append(d)
            except:
                pass
        print('num unique videos',len(unique_videos))
        for video in unique_videos:
            serializer = VideoDataSerializer(data=video)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        time.sleep(10)
    return None



class VideosList(generics.ListAPIView):
    serializer_class = VideoDataSerializer
    queryset = VideoData.objects.order_by('-publish_date')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination


youtube_data()

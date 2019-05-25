from django.http import HttpResponse
from django.shortcuts import render
import api
from django.core.paginator import Paginator

# Create your views here.
from django.views import generic


def index(request):
    return HttpResponse(" Landing Page of the site !!")


class VideosListView(generic.ListView):
    model = api.models.VideoData
    context_object_name = 'all_videos'
    template_name = r'landing/video_list.html'

    def get_queryset(self):
        return api.models.VideoData.objects.order_by('-publish_date')

class VideoDetailView(generic.DetailView):
    template_name = r'landing/video_detail.html'
    model = api.models.VideoData
    context_object_name = 'video'

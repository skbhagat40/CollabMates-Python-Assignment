from django.http import HttpResponse
from django.shortcuts import render
import api
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from .forms import FilterForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        user_form = FilterForm()
        context = super(VideosListView,self).get_context_data(**kwargs)
        context['user_form'] = user_form
        return context
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if 'selected_filter' in request.GET:
            to_apply = request.GET.get('selected_filter')
            context = {}
            context['all_videos'] =  api.models.VideoData.objects.order_by(to_apply)
            context['user_form'] = FilterForm()
            return render(request,'landing/video_list.html',context)
        else:
            return super(VideosListView,self).get(request)


class VideoDetailView(generic.DetailView):
    template_name = r'landing/video_detail.html'
    model = api.models.VideoData
    context_object_name = 'video'

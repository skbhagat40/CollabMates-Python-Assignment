from django.urls import path, include
from . import views
app_name = 'landing'

urlpatterns = [
    path('', views.index, name="index"),
    path('videos/', views.VideosListView.as_view(), name='videos_list'),
    path('videos/<int:pk>/', views.VideoDetailView.as_view(), name='video_detail')
]

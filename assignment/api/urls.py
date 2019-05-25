from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('get/', views.VideosList.as_view(), name="api_get")
    ]
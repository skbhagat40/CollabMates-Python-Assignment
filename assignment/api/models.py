from django.db import models


# Create your models here.
class VideoData(models.Model):
    video_id = models.CharField(verbose_name="video id", max_length=1000)
    title = models.CharField(verbose_name="video title", max_length=500)
    description = models.TextField(verbose_name="video description",blank=True)
    publish_date = models.DateTimeField(verbose_name="publishing Date Time")
    thumbnail_url = models.URLField(verbose_name="thumbnail url")

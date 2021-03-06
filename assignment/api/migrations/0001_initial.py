# Generated by Django 2.2.1 on 2019-05-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=1000, verbose_name='video id')),
                ('title', models.CharField(max_length=500, verbose_name='video title')),
                ('description', models.TextField(blank=True, verbose_name='video description')),
                ('publish_date', models.DateTimeField(verbose_name='publishing Date Time')),
                ('thumbnail_url', models.URLField(verbose_name='thumbnail url')),
            ],
        ),
    ]

from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(null=True, blank=True, max_length=100)


class Comment(models.Model):
    video_id = models.CharField(null=True, blank=True, max_length=100)
    comment = models.CharField(max_length=250)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)


class Reply(models.Model):
    video_id = models.CharField(null=True, blank=True, max_length=100)
    comment_pk = models.IntegerField(null=True, blank=True)
    reply = models.CharField(max_length=200, null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)
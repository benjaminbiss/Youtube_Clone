from rest_framework import serializers
from .models import Video, Comment, Reply

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_id']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
<<<<<<< HEAD
        fields = ['id', 'video_id', 'comment', 'likes', 'dislikes']
=======
        fields = ['id', 'video_id', 'video_pk', 'comment', 'likes', 'dislikes']
>>>>>>> 70ff97b8f5c9a4ecbd92cabf8655acfe07c51824
        
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'video_id','comment_pk', 'reply', 'likes', 'dislikes']
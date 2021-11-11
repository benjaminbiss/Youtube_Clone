from rest_framework import serializers
from .models import Video, Comment, Reply

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_id']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video_id', 'comment', 'likes', 'dislikes']
<<<<<<< HEAD
        
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'video_id', 'comment_pk', 'reply', 'likes', 'dislikes']
=======
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'video_id','comment_pk', 'reply', 'likes', 'dislikes']
>>>>>>> 8f7dac78870a7cf4d0e08189032a9acc80703721

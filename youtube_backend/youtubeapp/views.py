from django.http import request
from .models import Video, Comment, Reply
from .serializers import VideoSerializer, CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

class VideoList(APIView):

    def get(self, reqest):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk):
        update_video = self.get_object(pk)
        serializer = VideoSerializer(update_video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_video = self.get_object(pk)
        delete_video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentList(APIView):

    def get(self, reqest):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        update_comment = self.get_object(pk)
        serializer = CommentSerializer(update_comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_comment = self.get_object(pk)
        delete_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReplyList(APIView):

    def get(self, reqest):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        reply = self.get_object(pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)

    def put(self, request, pk):
        update_reply = self.get_object(pk)
        serializer = ReplySerializer(update_reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_reply = self.get_object(pk)
        delete_reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
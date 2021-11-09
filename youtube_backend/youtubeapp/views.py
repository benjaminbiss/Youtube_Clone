from django.shortcuts import render
from models import Video, Comment, Reply
from .serializers import VideoSerializer, CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status


from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoList.as_view()),
    path('video/<int:pk>/', views.VideoDetail.as_view()),
    path('video/<int:video_pk>/', views.CommentList.as_view()),
    path('video/<int:video_pk>/<int:pk>/', views.CommentDetail.as_view()),
    path('video/<int:video_pk>/<int:comment_pk>/', views.ReplyList.as_view()),
    path('video/<int:video_pk>/<int:comment_pk>/<int:pk>/', views.ReplyDetail.as_view())
]
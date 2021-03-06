from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoList.as_view()),
    path('video/<int:pk>/', views.VideoDetail.as_view()),
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('reply/<int:pk>/', views.ReplyDetail.as_view())
]
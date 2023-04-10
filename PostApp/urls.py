from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from PostApp.views import PostViewSet, create_post, LikeViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename="posts")
router.register('likes', LikeViewSet, basename="post_likes")
router.register('comments', CommentViewSet, basename="post_comments")

urlpatterns = [
    path('', include(router.urls)),
    path('create_post/', create_post),
]
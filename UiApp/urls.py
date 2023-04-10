from django.urls import path
from UiApp.views import index, timeline, my_posts, profile, login, post

urlpatterns = [
    path("", index),
    path("login", login, name="login"),
    path("my-posts", my_posts, name="posts"),
    path("post", post, name="single-post"),
    path("profile", profile, name="profile"),
    path("timeline", timeline, name="timeline"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts", views.all_posts, name="allposts"),
    path("posts/<id>", views.view_post, name="post"),
]

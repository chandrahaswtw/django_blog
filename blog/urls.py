from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("posts", views.AllPostsView.as_view(), name="allposts"),
    path("create", views.CreatePost.as_view(), name="createpost"),
    path("posts/<slug:slug>", views.PostView.as_view(), name="post"),
    path("posts/delete/<int:pk>", views.PostDeleteView.as_view(), name="deletepost"),
    path("posts/update/<int:pk>", views.PostUpdateView.as_view(), name="updatepost"),
]

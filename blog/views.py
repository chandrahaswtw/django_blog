from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/all_posts.html", {"posts": posts})


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(post.tags.all())
    return render(request, "blog/single_post.html", {"post": post})

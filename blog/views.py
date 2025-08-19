import os
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        base_query = super().get_queryset()
        records = base_query.all()[:3]
        return records


class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "posts"


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy("allposts")


class PostView(DetailView):
    template_name = "blog/single_post.html"
    model = Post
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "post"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("allposts")

    def form_valid(self, form):
        record = self.object
        if record.image and os.path.isfile(record.image.path):
            os.remove(record.image.path)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy("allposts")

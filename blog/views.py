import os
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        base_query = super().get_queryset()
        records = (
            base_query.filter(author=self.request.user)[:3]
            if self.request.user.is_authenticated
            else []
        )
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

    def form_valid(self, form):
        instance = form.instance
        instance.author = self.request.user
        messages.success(self.request, "Post created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


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
        messages.success(self.request, "Post deleted successfully!")
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy("allposts")

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully!")
        return super().form_valid(form)

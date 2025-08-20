from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=20)
    excerpt = models.CharField(max_length=50)
    image = models.FileField(upload_to="images")
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField("Tag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

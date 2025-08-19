from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=20)
    excerpt = models.CharField(max_length=50)
    image = models.FileField(upload_to="images")
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
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


# Create your models here.

from django.contrib import admin
from .models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "excerpt")


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

# Register your models here.

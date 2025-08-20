from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["created_at", "updated_at", "slug", "author"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Editing an existing object
            self.fields["image"].required = False
        else:
            # Creating a new object
            self.fields["image"].required = True

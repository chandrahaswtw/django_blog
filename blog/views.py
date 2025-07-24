from django.shortcuts import render
from django.http import Http404

posts = [
    {
        "id": "1",
        "image": "nature.png",
        "title": "Nature at it's best",
        "description": "Endless beauty, calming presence, diverse life, ever-changing, deeply inspiring.",
        "updatedAt": "10 March 2022",
    },
    {
        "id": "2",
        "image": "hiking.png",
        "title": "Mountain hiking",
        "description": "Adventure-filled trek through wilderness, energizing body, mind, and soul.",
        "updatedAt": "11 March 2022",
    },
    {
        "id": "3",
        "image": "coding.png",
        "title": "Coding is great!",
        "description": "Creating logic with language, solving problems, building digital worlds efficiently.",
        "updatedAt": "12 March 2022",
    },
]


def home(request):
    return render(request, "blog/home.html", {"posts": posts})


def all_posts(request):
    return render(request, "blog/all_posts.html", {"posts": posts})


def view_post(request, id):
    post = next((post for post in posts if post["id"] == id), None)
    if post:
        return render(request, "blog/single_post.html", {"post": post})
    raise Http404()

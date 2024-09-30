from django.shortcuts import render
import os
from blog.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html", {"title": "about"})

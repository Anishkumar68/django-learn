from django.shortcuts import render
import os
from blog.models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-published_at"]


class PostDetailedView(DetailView):
    model = Post


def about(request):
    return render(request, "blog/about.html", {"title": "about"})

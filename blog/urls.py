from django.urls import path
from .views import PostListView, PostDetailedView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailedView.as_view(), name="post-detail"),
    path("about/", views.about, name="about"),
]

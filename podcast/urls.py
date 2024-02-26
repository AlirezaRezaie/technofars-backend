from django.urls import path
from .views import PodcastListView, PodcastDetailView
from django.urls import path, re_path

urlpatterns = [
    path("", PodcastListView.as_view(), name="podcast-list"),
    re_path(r"(?P<slug>[^/]+)/?$", PodcastDetailView.as_view(), name="podcast-detail"),
]

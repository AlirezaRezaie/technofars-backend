from django.urls import path
from .views import ProjectListView, ProjectDetailView
from django.urls import path, re_path

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    re_path(r"(?P<slug>[^/]+)/?$", ProjectDetailView.as_view(), name="project-detail"),
]

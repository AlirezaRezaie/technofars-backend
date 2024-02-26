from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectTypeView
from django.urls import path, re_path

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    re_path(r"(?P<slug>[^/]+)/?$", ProjectDetailView.as_view(), name="project-detail"),
    path("type/<str:type_name>/", ProjectTypeView.as_view(), name="project-type"),
]

from django.urls import path
from .views import PersonListView, PersonDetailView
from django.urls import path, re_path

urlpatterns = [
    path("", PersonListView.as_view(), name="person-list"),
    re_path(r"(?P<slug>[^/]+)/?$", PersonDetailView.as_view(), name="person-detail"),
]

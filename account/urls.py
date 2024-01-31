from django.urls import path
from .views import PersonListView
from django.urls import path, re_path

urlpatterns = [
    path("", PersonListView.as_view()),
]

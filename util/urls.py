from django.urls import path
from . import views


urlpatterns = [
    path("contactus/", views.ContactUsListCreateView.as_view()),
]

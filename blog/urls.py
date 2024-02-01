from django.urls import path
from .views import (
    BlogDetailView,
    CategoryListView,
    CategoryGetBlogs,
    BlogListView,
    CommentListCreateView,
)
from django.urls import path, re_path

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category-all"),
    path(
        "category/<str:category_name>/",
        CategoryGetBlogs.as_view(),
        name="blogs-by-category",
    ),
    path("", BlogListView.as_view(), name="blog-list"),
    re_path(r"(?P<slug>[^/]+)/?$", BlogDetailView.as_view(), name="blog-detail"),
    path("comment/", CommentListCreateView.as_view()),
]

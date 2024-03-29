from django.urls import path
from .views import BlogRetrieveUpdateDestroyView
from .views import (
    BlogDetailView,
    CategoryCreateView,
    CategoryGetBlogs,
    BlogCreateView,
    BlogListView,
    CategoryRetrieveUpdateDestroyView,
    CommentListCreateView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="blog-crud"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog-crud"),
    path("update/<int:pk>/", BlogRetrieveUpdateDestroyView.as_view()),
    path("create/", BlogCreateView.as_view(), name="blog-crud"),
    path("comment/", CommentListCreateView.as_view()),
    path("category/", CategoryCreateView.as_view(), name="category-all"),
    path("category/<int:pk>/", CategoryRetrieveUpdateDestroyView.as_view()),
    path(
        "category/<str:category_name>/",
        CategoryGetBlogs.as_view(),
        name="blogs-by-category",
    ),
]

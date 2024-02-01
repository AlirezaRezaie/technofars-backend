from rest_framework import generics, permissions

from .models import Blog, Category, Comment
from .serializers import (
    BlogDetailSerializer,
    BlogListSerializer,
    CategorySerializer,
    CommentSerializer,
)
from django.shortcuts import get_object_or_404


# *-------Blog views-------*
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by("created_at")
    serializer_class = BlogListSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = "slug"


# *-------Category views-------*
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryGetBlogs(generics.ListAPIView):
    serializer_class = BlogDetailSerializer

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        category = get_object_or_404(Category, name=category_name)
        return Blog.objects.filter(categories=category.id)


# *-------Comment views-------*
class CommentsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

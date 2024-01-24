from rest_framework import generics
from .models import Blog, Category, Comment
from .serializers import (
    BlogSerializer,
    BlogDetailSerializer,
    BaseBlogListSerializer,
    CategorySerializer,
    CommentSerializer,
)
from django.shortcuts import get_object_or_404


# *-------Blog views-------*
# blog get all and create
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by("created_at")
    serializer_class = BaseBlogListSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer


# blog get all and create
class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# blog update , delete, and get by id
class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        print(self.request.method)
        if self.request.method == "GET":
            return BaseBlogListSerializer
        else:
            return BlogSerializer


# *-------Category views-------*
class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryGetBlogs(generics.ListAPIView):
    serializer_class = BaseBlogListSerializer

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

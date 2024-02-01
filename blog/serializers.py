from rest_framework import serializers
from jdatetime import datetime as jdatetime

from .models import Blog, Category, Comment
from account.serializers import PersonProfileSerializer

# Convert Unix time to Persian date


class BlogDetailSerializer(serializers.ModelSerializer):
    author = PersonProfileSerializer(many=False)
    author_profile = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()  # New field for Persian date
    keyword = serializers.SerializerMethodField()  # New field for Persian date
    comments = serializers.SerializerMethodField()

    # ... (your existing code)

    class Meta:
        model = Blog
        fields = "__all__"  # Include the new field

    def get_keyword(self, obj):
        # "برنامه نویسی, پایتون, برنامه"
        # for meta frontend metatags
        all_keywords = [keyword.name for keyword in obj.keyword.all()]
        all_keywords = ", ".join(all_keywords)
        return all_keywords

    def get_categories(self, obj):
        return [category.name for category in obj.categories.all()]

    def get_author(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}"
        return None

    def get_author_profile(self, obj):
        if obj.author.profile_image:
            profile_image_url = self.context["request"].build_absolute_uri(
                obj.author.profile_image.url
            )
            return profile_image_url
        return None

    def get_comments(self, obj):
        comments = obj.comments.all()  # Get all comments related to this post
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_created_at(self, obj):
        # Assuming created_at is a DateTimeField in your model
        if obj.created_at:
            persian_time = jdatetime.fromgregorian(datetime=obj.created_at, locale="fa")
            return persian_time.strftime(
                "%A %d %B %H:%M"
            )  # Convert created_at to Persian date format

        return None  # Handle cases where created_at is None


class BlogListSerializer(serializers.ModelSerializer):
    author = PersonProfileSerializer(many=False)

    class Meta:
        model = Blog
        fields = ("title", "description", "image", "author", "slug")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("ip",)


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()  # New field for Persian date

    class Meta:
        model = Comment
        exclude = ("ip",)
        read_only_fields = ["created_at"]

    def get_created_at(self, obj):
        # Assuming created_at is a DateTimeField in your model
        if obj.created_at:
            persian_time = jdatetime.fromgregorian(datetime=obj.created_at, locale="fa")
            return persian_time.strftime(
                "%A %d %B %H:%M"
            )  # Convert created_at to Persian date format

        return None  # Handle cases where created_at is None

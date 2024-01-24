from rest_framework import serializers
from jdatetime import datetime as jdatetime

from .models import Blog, Category, Comment

# Convert Unix time to Persian date


class BaseBlogListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    author_profile = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()  # New field for Persian date
    # ... (your existing code)

    class Meta:
        model = Blog
        fields = "__all__"  # Include the new field

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

    def get_created_at(self, obj):
        # Assuming created_at is a DateTimeField in your model
        if obj.created_at:
            persian_time = jdatetime.fromgregorian(datetime=obj.created_at, locale="fa")
            return persian_time.strftime(
                "%A %d %B %H:%M"
            )  # Convert created_at to Persian date format

        return None  # Handle cases where created_at is None


class BlogDetailSerializer(BaseBlogListSerializer):
    comments = serializers.SerializerMethodField()

    class Meta(BaseBlogListSerializer.Meta):
        fields = (
            BaseBlogListSerializer.Meta.fields
        )  # Exclude 'post' for displaying comments

    # Your existing methods remain unchanged
    def get_comments(self, obj):
        comments = obj.comments.all()  # Get all comments related to this post
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


class BlogSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        return mark_safe(obj.your_text_field)

    class Meta:
        model = Blog
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def update(self, instance, validated_data):
        # Retrieve the existing image if available
        existing_image = instance.image
        # new instance to be created
        instance = super().update(instance, validated_data)

        # if there is no existing image and no new image instance
        if existing_image and not instance.image:
            instance.image = existing_image
        instance.save()

        return instance


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

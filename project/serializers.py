from rest_framework import serializers
from .models import Project, ProjectImage
from account.serializers import PersonListSerializer


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ("url",)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "thumbnail", "slug", "created_at")


class ProjectDetailSerializer(serializers.ModelSerializer):
    creators = PersonListSerializer(many=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"

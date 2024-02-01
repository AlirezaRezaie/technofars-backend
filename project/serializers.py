from rest_framework import serializers
from .models import Project
from account.serializers import PersonProfileSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "thumbnail", "slug")


class ProjectDetailSerializer(serializers.ModelSerializer):
    creators = PersonProfileSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"

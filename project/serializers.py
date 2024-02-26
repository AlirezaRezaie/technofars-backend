from rest_framework import serializers
from .models import Project, ProjectImage
from util.serializers import PersonProfileSerializer, TechnologySerializer


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ("url",)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ("title", "thumbnail", "slug", "created_at")


class ProjectDetailSerializer(serializers.ModelSerializer):
    creators = PersonProfileSerializer(many=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    technologies = TechnologySerializer(many=True)
    related_projects = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()

    def get_group(self, obj):
        return obj.group.name if obj.group else None

    def get_related_projects(self, obj):
        user_projects = []
        if obj.group:
            user_projects = Project.objects.filter(group__id=obj.group.id).exclude(
                id=obj.id
            )
        return ProjectSerializer(user_projects, many=True, context=self.context).data

    class Meta:
        model = Project
        fields = "__all__"

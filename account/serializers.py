from rest_framework import serializers

from project.models import Project
from project.serializers import ProjectSerializer
from util.serializers import TechnologySerializer

from .models import Person, Contact


# Convert Unix time to Persian date
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ("id", "contact_info")


class PersonListSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    contact = serializers.SerializerMethodField()

    def get_role(self, obj):
        if obj.role:
            return obj.role.name
        else:
            return None

        # Your existing methods remain unchanged

    def get_contact(self, obj):
        try:
            contact_instance = obj.contact
            if contact_instance:
                return ContactSerializer(contact_instance).data
            else:
                return None
        except Contact.DoesNotExist:
            return None

    class Meta:
        model = Person
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "profile_image",
            "about_me",
            "role",
            "contact",
            "slug",
        )


class PersonDetailSerializer(serializers.ModelSerializer):
    skills = TechnologySerializer(many=True)
    projects = serializers.SerializerMethodField()
    contact = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        if obj.role:
            return obj.role.name
        else:
            return None

    def get_projects(self, obj):
        user_projects = Project.objects.filter(creators=obj.id)
        return ProjectSerializer(user_projects, many=True, context=self.context).data

    def get_contact(self, obj):
        try:
            contact_instance = obj.contact
            if contact_instance:
                return ContactSerializer(contact_instance).data
            else:
                return None
        except Contact.DoesNotExist:
            return None

    class Meta:
        model = Person
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "profile_image",
            "about_me",
            "role",
            "contact",
            "skills",
            "biography",
            "projects",
        )

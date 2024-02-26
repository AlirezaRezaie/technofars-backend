# pylint: disable=W0223
from rest_framework import serializers
from account.models import Technology, Person

from .models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    """
    contact us sereilizer
    """

    class Meta:
        model = ContactUs
        fields = "__all__"


# multiple usage (global) serializrs
class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        exclude = ("id",)


class PersonProfileSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        if obj.role:
            return obj.role.name
        else:
            return None

    class Meta:
        model = Person
        fields = (
            "first_name",
            "last_name",
            "profile_image",
            "role",
            "slug",
        )

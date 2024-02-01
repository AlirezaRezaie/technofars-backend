from rest_framework import serializers
from .models import Person, Contact


# Convert Unix time to Persian date
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ("id", "contact_info")


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
        )


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
        )

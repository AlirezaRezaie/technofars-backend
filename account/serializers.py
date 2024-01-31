from rest_framework import serializers
from .models import Person

# Convert Unix time to Persian date


class PersonListSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    def get_role(self, obj):
        if obj.role:
            return obj.role.name
        else:
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
        )

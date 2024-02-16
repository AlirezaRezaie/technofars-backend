# pylint: disable=W0223

from rest_framework import serializers
from .models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    """
    contact us sereilizer
    """

    class Meta:
        model = ContactUs
        fields = "__all__"

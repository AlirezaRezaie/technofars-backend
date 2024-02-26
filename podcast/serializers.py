from rest_framework import serializers

from jdatetime import datetime as jdatetime

from .models import Podcast
from util.serializers import PersonProfileSerializer


class PodcastSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()  # New field for Persian date

    def get_created_at(self, obj):
        # Assuming created_at is a DateTimeField in your model
        if obj.created_at:
            persian_time = jdatetime.fromgregorian(datetime=obj.created_at, locale="fa")
            return persian_time.strftime(
                "%A %d %B %H:%M"
            )  # Convert created_at to Persian date format

        return None  # Handle cases where created_at is None

    class Meta:
        model = Podcast
        fields = ("title", "description", "thumbnail", "slug", "created_at")


class PodcastDetailSerializer(serializers.ModelSerializer):
    hosts = PersonProfileSerializer(many=True)

    class Meta:
        model = Podcast
        fields = "__all__"

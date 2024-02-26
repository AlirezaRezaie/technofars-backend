from rest_framework import serializers
from .models import Podcast
from util.serializers import PersonProfileSerializer


class PodcastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = ("title", "thumbnail", "slug", "created_at")


class PodcastDetailSerializer(serializers.ModelSerializer):
    hosts = PersonProfileSerializer(many=True)

    class Meta:
        model = Podcast
        fields = "__all__"

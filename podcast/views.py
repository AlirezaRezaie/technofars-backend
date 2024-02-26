from rest_framework import generics
from .models import Podcast

from .serializers import PodcastSerializer, PodcastDetailSerializer


# *-------podcast views-------*
class PodcastListView(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class PodcastDetailView(generics.RetrieveAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastDetailSerializer
    lookup_field = "slug"

from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer, ProjectDetailSerializer


# *-------Project views-------*
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = "slug"

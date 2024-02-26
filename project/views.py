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


class ProjectTypeView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        type_name = self.kwargs["type_name"]
        return Project.objects.filter(project_type=type_name)

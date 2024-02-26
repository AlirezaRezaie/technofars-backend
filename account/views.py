from rest_framework import generics
from .models import Person
from .serializers import PersonListSerializer, PersonDetailSerializer


# *-------Person views-------*
class PersonListView(generics.ListAPIView):
    queryset = Person.objects.all().order_by("created_at")
    serializer_class = PersonListSerializer


class PersonDetailView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer
    lookup_field = "slug"


# Create your views here.

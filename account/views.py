from rest_framework import generics
from .models import Person
from .serializers import PersonListSerializer


# *-------Person views-------*
class PersonListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer


# Create your views here.

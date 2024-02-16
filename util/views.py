from rest_framework.generics import (
    ListCreateAPIView,
)


from .models import ContactUs
from .serializers import ContactUsSerializer


class ContactUsListCreateView(ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

from rest_framework import generics, viewsets
from muvision.models import Exposition
from .serializers import ExpositionSerializer


class ExpositionAPIView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ExpositionSerializer
    queryset = Exposition.objects.all()


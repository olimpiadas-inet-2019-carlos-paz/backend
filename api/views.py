from rest_framework import viewsets
from muvision.models import Exposition
from .serializers import ExpositionSerializer


class ExpositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exposition.objects.all().order_by('name')
    serializer_class = ExpositionSerializer

from rest_framework import serializers
from muvision.models import Exposition


class ExpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposition
        fields = ['id', 'name', 'creation_date', 'description', 'img_url']

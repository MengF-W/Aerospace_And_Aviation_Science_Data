
from rest_framework import serializers

from nasaApp.models import APOD


class APODSerializer(serializers.ModelSerializer):
    class Meta:
        model = APOD
        fields = ['id', 'date', 'title','media_type','media_location','explanation','credit','copyright','alt']
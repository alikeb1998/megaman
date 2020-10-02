from . import models
from rest_framework import serializers


class FisheSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Fish
        fields = ("name", "active", "created")

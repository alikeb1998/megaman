from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


# Create your views here.
class FishViewSet(viewsets.ModelViewSet):
    queryset = models.Fish.objects.all()
    serializer_class = serializers.FisheSerializer

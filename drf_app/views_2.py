from rest_framework import viewsets

from drf_app.models import Film, Actor
from drf_app.serializers_2 import FilmSerializer, ActorSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


from rest_framework import generics

from drf_app.models import Film, Actor
from drf_app.serializers_2 import FilmSerializer, ActorSerializer


class FilmAPIList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmAPIUpdate(generics.UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class ActorAPIList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorAPIUpdate(generics.UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

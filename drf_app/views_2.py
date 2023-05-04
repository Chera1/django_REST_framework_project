from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_app.models import Film, Actor, ActorFilmWork
from drf_app.serializers_2 import FilmSerializer, ActorSerializer


class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Film.objects.all()[:3]

        return Film.objects.filter(pk=pk)

    @action(methods=['get'], detail=True, description='Returns the full name of all actors in the current film')
    def actors_name(self, request, pk):
        """
        Returns the full name of all actors in the current film
        """
        relative_model_data = list(ActorFilmWork.objects.filter(films_id=pk))
        return Response({'actors': [obj.actor.full_name for obj in relative_model_data]})

    @action(methods=['get'], detail=False, description='Return a type selection from the "type" field Model Film')
    def type_choices(self, request):
        """
        Return a type selection from the "type" field Model Film
        """
        return Response({'type_choices': Film.type.field.choices})


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Actor.objects.all()[:3]

        return Actor.objects.filter(pk=pk)

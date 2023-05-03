from rest_framework.response import Response
from rest_framework.views import APIView

from drf_app.models import Film, Actor, ActorFilmWork
from drf_app.serializers import FilmSerializer, ActorSerializer, ActorFilmWorkSerializer


class FilmAPIView(APIView):
    def get(self, request):
        queryset = Film.objects.all()
        serializer_for_queryset = FilmSerializer(
            instance=queryset,
            many=True
        )
        return Response({"films_list": serializer_for_queryset.data})

    def post(self, request):
        serializer_film = FilmSerializer(data=request.data)
        serializer_film.is_valid(raise_exception=True)
        serializer_film.save()

        return Response({'film': serializer_film.data})

    def put(self, request, *arg, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Film.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        serializer = FilmSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'film': serializer.data})

    def delete(self, request, *arg, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Film.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        instance.delete()
        return Response({'film': "deleted film " + str(pk)})


class ActorAPIView(APIView):
    def get(self, request):
        queryset = Actor.objects.all()
        serializer_for_queryset = ActorSerializer(
            instance=queryset,
            many=True
        )
        return Response({"actors_list": serializer_for_queryset.data})

    def post(self, request):
        serializer_actor = ActorSerializer(data=request.data)
        serializer_actor.is_valid(raise_exception=True)
        serializer_actor.save()

        return Response({'actor': serializer_actor.data})

    def put(self, request, *arg, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Actor.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        serializer = ActorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'actor': serializer.data})

    def delete(self, request, *arg, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Actor.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        instance.delete()
        return Response({'actor': "deleted actor " + str(pk)})

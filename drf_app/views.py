from rest_framework.response import Response
from rest_framework.views import APIView

from drf_app.models import Film, Actor, ActorFilmWork
from drf_app.serializers import FilmSerializer


class FilmAPIView(APIView):
    def get(self, request):
        queryset = Film.objects.all()
        serializer_for_queryset = FilmSerializer(
            instance=queryset,
            many=True
        )
        return Response({"films_list": serializer_for_queryset.data})

    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Creating film if it needed
        new_film = Film.objects.get_or_create(
            name=request.data['name'],
            type=request.data['type'],
        )

        actors = request.data['actors']
        if actors:
            # Creating actors if it needed
            for each_act in actors:
                new_actor = Actor.objects.get_or_create(
                    full_name=each_act['full_name'],
                    age=each_act['age']
                )
                # Creating related records
                ActorFilmWork.objects.create(
                    films_id=new_film[0].id,
                    actor_id=new_actor[0].id
                )

        serializer_for_queryset = FilmSerializer(
            instance=new_film[0]
        )
        return Response({'film': serializer_for_queryset.data})

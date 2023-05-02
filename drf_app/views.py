from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_app.models import Film
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
        new_film = Film.objects.create(
            name=request.data['name'],
            type=request.data['type']
        )
        return Response({'film': model_to_dict(new_film)})

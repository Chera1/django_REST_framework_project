from rest_framework import generics
from django.shortcuts import render

from drf_app.models import Film
from drf_app.serializers import FilmSerializer


class FilmAPIView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

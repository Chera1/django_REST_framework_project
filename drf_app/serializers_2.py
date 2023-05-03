# 2 method of serializer
from rest_framework import serializers

from drf_app.models import Film, Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('full_name', 'age')


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('name', 'type', 'actors')

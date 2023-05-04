# 2 method of serializer
from rest_framework import serializers

from drf_app.models import Film, Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class FilmSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Film
        fields = "__all__"

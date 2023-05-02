from rest_framework import serializers

from drf_app.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('name', 'type')

from rest_framework import serializers


class ActorSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(allow_null=True)


class FilmSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=100)
    actors = ActorSerializer(many=True)


class ActorFilmWorkSerializer(serializers.Serializer):
    films = FilmSerializer()
    actor = ActorSerializer()
    role = serializers.CharField(max_length=255, allow_null=True)

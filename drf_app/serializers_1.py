# 1 method of serializer
from rest_framework import serializers

from drf_app.models import Film, Actor


class ActorSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class FilmSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Film.objects.create(name=validated_data['name'], type=validated_data['type'])

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance


# class ActorFilmWorkSerializer(serializers.Serializer):
#     films = FilmSerializer()
#     actor = ActorSerializer()
#     role = serializers.CharField(max_length=255, allow_null=True)

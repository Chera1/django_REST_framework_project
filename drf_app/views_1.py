from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from drf_app.models import Film, Actor
from drf_app.permissions import IsAdminOrReadOnly
from drf_app.serializers_2 import FilmSerializer, ActorSerializer


class FilmAPIList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class FilmAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )  # авторизация исключительно по токену


class FilmAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ActorAPIList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ActorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)  # авторизация исключительно по токену


class ActorAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAdminOrReadOnly,)

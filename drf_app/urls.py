from django.urls import path

from . import views_1
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'films', views_2.FilmViewSet, basename='film')
# router.register(r'actors', views_2.ActorViewSet, basename='actor')

urlpatterns = [
    path('api/films/', views_1.FilmAPIList.as_view()),
    path('api/film/<int:pk>', views_1.FilmAPIUpdate.as_view()),
    path('api/filmdelete/<int:pk>', views_1.FilmAPIDelete.as_view()),
    path('api/actors/', views_1.ActorAPIList.as_view()),
    path('api/actor/<int:pk>', views_1.ActorAPIUpdate.as_view()),
    path('api/actordelete/<int:pk>', views_1.ActorAPIDelete.as_view()),
]

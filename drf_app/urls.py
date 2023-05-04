from django.urls import path, include

from . import views_2
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'films', views_2.FilmViewSet)
router.register(r'actors', views_2.ActorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/(films/actors)/
]

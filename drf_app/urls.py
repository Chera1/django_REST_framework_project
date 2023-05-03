from django.urls import path

from . import views

urlpatterns = [
    path('api/films/', views.FilmAPIView.as_view()),
    path('api/actors/', views.ActorAPIView.as_view()),
    path('api/films/<int:pk>', views.FilmAPIView.as_view()),
    path('api/actors/<int:pk>', views.ActorAPIView.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path('api/films/', views.FilmAPIView.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path('api/films/', views.FilmAPIView.as_view()),
    # path('', views.main_page, name='main_page'),
]

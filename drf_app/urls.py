from django.urls import path

from . import views

urlpatterns = [
    path('api/films/', views.FilmAPIList.as_view()),
    path('api/actors/', views.ActorAPIList.as_view()),
    path('api/films/<int:pk>', views.FilmAPIUpdate.as_view()),
    path('api/filmsdetail/<int:pk>', views.FilmAPIDetailView.as_view()),
    path('api/actorsdetail/<int:pk>', views.ActorAPIDetailView.as_view()),
    path('api/actors/<int:pk>', views.ActorAPIUpdate.as_view()),
]

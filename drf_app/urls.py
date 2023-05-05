from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views_1
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'films', views_2.FilmViewSet, basename='film')
# router.register(r'actors', views_2.ActorViewSet, basename='actor')

urlpatterns = [
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/films/', views_1.FilmAPIList.as_view()),
    path('api/film/<int:pk>', views_1.FilmAPIUpdate.as_view()),
    path('api/filmdelete/<int:pk>', views_1.FilmAPIDelete.as_view()),
    path('api/actors/', views_1.ActorAPIList.as_view()),
    path('api/actor/<int:pk>', views_1.ActorAPIUpdate.as_view()),
    path('api/actordelete/<int:pk>', views_1.ActorAPIDelete.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

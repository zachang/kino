from django.urls import path

from .views import films, film, home

app_name = 'cinema'
urlpatterns = [
    path('', home, name='home'),
    path('movies/', films, name='films'),
    path('movies/<str:movie_id>/', film, name='film'),
]

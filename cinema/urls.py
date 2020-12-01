from django.urls import path

from .views import films, film

app_name = 'cinema'
urlpatterns = [
    path('', films, name='films'),
    path('<str:movie_id>/', film, name='film'),
]

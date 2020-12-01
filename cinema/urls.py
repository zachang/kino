from django.urls import path

from .views import films

app_name = 'cinema'
urlpatterns = [
    path('', films, name='films'),
]
from django.conf import settings
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods

from cinema.service import get_movies, get_movie


@require_http_methods(["GET"])
def home(request):
    return render(request, 'cinema/home.html')


@cache_page(settings.CACHE_TTL)
@require_http_methods(['GET'])  # with DRF this would be @api_view(['GET'])
def films(request):
    """Resource view for all movies"""
    movies_list = get_movies()
    page = request.GET.get('page', 1)
    paginator = Paginator(movies_list, 10)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    context = {'movies': movies}
    return render(request, 'cinema/movies.html', context)


@cache_page(settings.CACHE_TTL)
@require_http_methods(['GET'])  # with DRF this would be @api_view(['GET'])
def film(request, movie_id):
    """Resource view for a single movie"""
    movie = get_movie(movie_id)
    return render(request, 'cinema/movie.html', {'movie': movie})

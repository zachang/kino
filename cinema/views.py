from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.shortcuts import render

from cinema.service import get_movies, get_movie


def films(request):
    movies_list = get_movies()
    page = request.GET.get('page', 1)
    paginator = Paginator(movies_list, 10)
    if movies_list:
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)

        return render(request, 'cinema/movies.html', {'movies': movies})
    return render(request, 'cinema/movies.html', {'movies': movies_list})


async def film(request, movie_id):
    movie = await get_movie(movie_id)
    return render(request, 'cinema/movie.html', {'movie': movie})

import requests

MOVIE_URL = 'https://ghibliapi.herokuapp.com/films/'


def get_movies():
    response = requests.get(MOVIE_URL)
    movies = response.json() if response.status_code == 200 else []

    return movies

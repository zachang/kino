import requests

MOVIE_URL = 'https://ghibliapi.herokuapp.com/films/'
CAST_URL = 'https://ghibliapi.herokuapp.com/people/'


def get_movies():
    response = requests.get(MOVIE_URL)
    movies = response.json() if response.status_code == 200 else []

    return movies


def get_movie(movie_id):
    movie_response = requests.get(f'{MOVIE_URL}{movie_id}')
    if movie_response.status_code == 200:
        people_response = requests.get(CAST_URL)
        movie = movie_response.json()
        people = people_response.json()
        casts = (cast['name'] for cast in people if movie_id in ','.join(cast['films']))
        movie['casts'] = list(casts)
        return movie
    return []

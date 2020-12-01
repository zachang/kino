import requests
import httpx

MOVIE_URL = 'https://ghibliapi.herokuapp.com/films/'
CAST_URL = 'https://ghibliapi.herokuapp.com/people/'


def get_movies():
    response = requests.get(MOVIE_URL)
    movies = response.json() if response.status_code == 200 else []

    return movies


async def get_movie(movie_id):
    async with httpx.AsyncClient() as client:
        movie_response = await client.get(f'{MOVIE_URL}{movie_id}')
        people_response = await client.get(CAST_URL)
        movie = movie_response.json()
        people = people_response.json()
        casts = (cast['name'] for cast in people if movie_id in ','.join(cast['films']))
        movie['casts'] = casts
        return movie

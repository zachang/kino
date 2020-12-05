import requests


from requests_toolbelt import sessions
from urllib3.util.retry import Retry

from cinema.timeout_adapter import TimeoutHTTPAdapter

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)

MOVIE_URL = '/films/'
CAST_URL = '/people/'
http = sessions.BaseUrlSession(base_url='https://ghibliapi.herokuapp.com')

# Mount it for both http and https usage
adapter = TimeoutHTTPAdapter(timeout=5, max_retries=retry_strategy)
http.mount("https://", adapter)


def get_movies():
    """All movies api call"""
    response = http.get(MOVIE_URL)
    movies = response.json() if response.status_code == requests.codes.ok else []
    return movies


def get_movie(movie_id):
    """Specific movie api call
    :param movie_id: The specific movie resource.
    """
    movie_response = http.get(f'{MOVIE_URL}{movie_id}')
    if movie_response.status_code == requests.codes.ok:
        people_response = http.get(CAST_URL)
        movie = movie_response.json()
        people = people_response.json()
        casts = (cast['name'] for cast in people if movie_id in ','.join(cast['films']))
        movie['casts'] = list(casts)
        return movie
    return []

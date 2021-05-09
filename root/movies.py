import random
import requests
from django.conf import settings


def get_movies_ids(number):
    ids = settings.MOVIES
    movies_ids = random.choices(ids, k=number)
    return movies_ids


def get_movies_list(size=15):
    movies_list = []
    movies = get_movies_ids(size)
    for id_movie in movies:
        movie = get_movie(id_movie)
        if movie != -1:
            movies_list.append(get_movie(id_movie))
    return movies_list


def get_movie(movie_id):
    url = 'http://www.omdbapi.com/'
    param = {'apikey': settings.OMBD_API_KEY, 'i': movie_id}
    try:
        data = requests.get(url, params=param)
    except:
        return {}
    if str(data.json()).find('Incorrect IMDb ID') > 0:
        return -1
    return data.json()

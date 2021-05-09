import random

import requests
from django.conf import settings


def get_movies_ids(number, low, high):
    movies_low = random.sample(settings.MOVIES_LOW, k=low)
    movies_high = random.choices(settings.MOVIES_HIGH, k=high)
    movies_other = random.choices(
        list(set(settings.MOVIES) - set(movies_high) - set(movies_low)),
        k=(number - low - high))
    return movies_other + movies_high + movies_low


def get_movies_list(size, low, high):
    movies_list = []
    movies = get_movies_ids(size, low, high)
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

import requests
from django.conf import settings

MOVIES = ['tt0078748', 'tt1396484', 'tt0340855', 'tt2784512', 'tt3297314', 'tt1663655', 'tt0120841', 'tt9173418',
          'tt0437179', 'tt0440803', 'tt0374563', 'tt0192731', 'tt0455857', 'tt0282209', 'tt5690360']

OMBD_API_KEY = "4c82f8b8"


def get_movies_list():
    movies_list = []
    #for id_movie in settings.MOVIES:
    for id_movie in MOVIES:
        movies_list.append(get_movie(id_movie))
    return movies_list


def get_movie(movie_id):
    url = 'http://www.omdbapi.com/'
    #param = {'apikey': settings.OMBD_API_KEY, 'i': movie_id}
    param = {'apikey': '4c82f8b8', 'i': movie_id}
    try:
        data = requests.get(url, params=param)
    except:
        return {}
    return data.json()


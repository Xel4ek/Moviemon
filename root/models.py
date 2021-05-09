import logging
import pathlib
import pickle
import random
import glob
import re

from django.db import models

# Create your models here.
from django.http import Http404

from . import db, movies
from .classes import Game, Moviemon

'''
• ’load’: Load the game data passed in parameters in the class instance. Returns the
current instance.
• ’dump’: Returns the game’s data.
• ’get_random_movie’: Returns a random Moviemon among the Moviemons not yet
captured.
• ’load_default_settings’: Loads the game data in the class instance from the settings. Requests and stocks all the Moviemons details on IMDB. Returns the current
intance.
• ’get_strength’: Returns the player’s strength.
• ’get_movie’: Returns a Python dictionary containing all the det'''


class Supplier:
    _settings = {
        'start_x': 1,
        'start_y': 8,
        'size': 10,
        'max_moviemons': 15,
        'max_balls': 30
    }
    _remote_api = movies.get_movies_list(_settings.get('max_moviemons'))
    _game = None
    @staticmethod
    def game() -> Game:
        return Supplier._game if Supplier._game else Supplier.load()
    @staticmethod
    def info():
        files = [filename.split('\\')[-1].split('/')[-1] for filename in glob.glob("root/save_game/slot*.mmg")]
        print(files)
        def get_file(slot):
            file = list(filter(lambda x: 'slot' + str(slot) in x, files))
            return '/'.join(file[0].split('.')[0].split('_')[1:3]) if len(file) else 'free'
        return {key: get_file(key) for key in ['a', 'b', 'c']}

    @staticmethod
    def load(slot='game.mmg'):
        if slot != 'game.mmg':
            files = [filename.split('\\')[-1].split('/')[-1] for filename in glob.glob("root/save_game/slot{}*.mmg".format(slot))]
            file = list(filter(lambda x: 'slot' + str(slot) in x, files))
        else:
            file = [slot]
        try:
            with open(pathlib.Path('root', 'save_game', file[0]), 'rb') as f:
                Supplier._game = pickle.load(f)
        except Exception as e:
            logging.error(e)

    @staticmethod
    def dump(slot='game.mmg'):
        if slot != 'game.mmg':
            filename = 'slot{}_{}_{}.mmg'.format(slot, Supplier._game.count_caught_moviemons(), Supplier._game.count_moviemons())
            to_clear = glob.glob('root/save_game/slot{}*.mmg'.format(slot))
            try:
                [pathlib.Path(file).unlink() for file in to_clear]
            except OSError as e:
                print("Ошибка!")
        else:
            filename = slot
        try:
            with open(pathlib.Path('root', 'save_game', filename), 'wb') as f:
                pickle.dump(Supplier._game, f)
        except Exception as e:
            logging.error(e)


    @staticmethod
    def get_random_movie():
        pass

    @staticmethod
    def new_game():
        Supplier._game = Game([Moviemon.from_movie(movie) for movie in Supplier._remote_api], Supplier.load_default_settings())

    @staticmethod
    def load_default_settings():
        return {'grid_size_x': Supplier._settings.get('size'), 'grid_size_y': Supplier._settings.get('size'),
                **Supplier._settings}

    @staticmethod
    def get_strength():
        return Supplier.game().strength()

    @staticmethod
    def get_movie():
        pass

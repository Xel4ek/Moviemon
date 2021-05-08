from django.db import models

# Create your models here.
from .settings import settings

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
    __settings = settings

    @staticmethod
    def load():
        pass

    @staticmethod
    def dump():
        pass

    @staticmethod
    def get_random_movie():
        pass

    @staticmethod
    def load_default_settings():
        return {'grid_size_x': Supplier.__settings.get('grid_size_x'), 'grid_size_y': Supplier.__settings.get('grid_size_y'),
                'start_x': Supplier.__settings.get('start_x'), 'start_y': Supplier.__settings.get('start_y')}

    @staticmethod
    def get_strength():
        pass

    @staticmethod
    def get_movie():
        pass

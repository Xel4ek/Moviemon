'''
Description : Title screen.
• Screen: Must display the game’s title as well as ’A - New Game’ and ’B - Load’.
• Url: basic one, domain name and port.
• Controls:
◦ A: A link to the Worldmap page.
Before it’s being displayed, the file containing the current game informations
must be reinitialized with the Settings parameters and the Moviemons must
be requested once again.
◦ B: link to the Load page.
'''
import random

from .models import Supplier
from .tools import Render


def index(request):
    return Render(request).render()


def save_game(request):
    pass


def load_game(request):
    pass


def moviemon(request):
    pass


def worldmap(request):
    default = Supplier.load_default_settings()
    max_x = default.get('grid_size_x')
    max_y = default.get('grid_size_y')
    player = default.get('start_x'), default.get('start_y')

    def is_player(n):
        return n % max_x == player[0] and n // max_y == player[1]
    def coin():
        return random.choice([True, False])
    map_list = [{'x': n % max_x, 'y': n // max_y, 'player': is_player(n), 'ball': coin(), 'pokemon': coin()} for n in range(max_x * max_y)]
    settings = {**default, 'map_list': map_list}

    return Render(request, 'worldmap', {'settings': settings})


def battle(request):
    pass


def moviedex(request):
    pass


def detail(request):
    pass


def options(request):
    pass

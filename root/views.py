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
    help_list = ['a: new game', 'b: load']
    actions = {'a': {'url': 'worldmap', 'par': 'new'}, 'b': {'url': 'load_game', 'par': 0}}
    return Render(request, context={'help': help_list}, actions=actions).render()


def save_game(request, slot=3):
    magic = 123

    def is_selected(i):
        return slot % 3 == ord(i) - ord('a')

    if slot > 3:
        Supplier.dump(chr(ord('a') + slot - magic))
        slot -= magic

    slots = [{'text': 'slot ' + key + ':' + value, 'selected': is_selected(key)} for (key, value) in
             Supplier.info.items()]
    help_list = ['a: save', 'b: cancel']
    actions = {
        'up': {'url': 'save_game', 'par': (slot - 1) % 3}, 'down': {'url': 'save_game', 'par': (slot + 1) % 3},
        'a': {'url': 'save_game', 'par': slot + magic}
    }

    return Render(request, 'save', context={'help': help_list, 'slots': slots, 'selected': slot % 3},
                  actions=actions).render()


def load_game(request, slot=0):
    def is_selected(i):
        return slot % 3 == ord(i) - ord('a')

    slots = [{'text': 'slot ' + key + ':' + value, 'selected': is_selected(key)} for (key, value) in
             Supplier.info.items()]
    help_list = ['a: load', 'b: cancel']
    actions = {'up': {'url': 'load_game', 'par': (slot - 1) % 3}, 'down': {'url': 'load_game', 'par': (slot + 1) % 3}}
    return Render(request, 'save', context={'help': help_list, 'slots': slots, 'selected': slot % 3},
                  actions=actions).render()


def moviemon(request):
    pass


def worldmap(request, new=None):
    default = Supplier.load_default_settings()
    max_x = default.get('grid_size_x')
    max_y = default.get('grid_size_y')

    # 'x': n % max_x, 'y': n // max_y,
    if new:
        Supplier.new_game()

    map_list = Supplier.game.map.items
    settings = {**default, 'map_list': map_list, 'balls': 6, 'message': ['Lorem dwadaw ', 'dawdawdawdaw']}
    # TODO: set moviemon_id on move
    moviemon_id = None
    actions = {
        'up': {'url': 'worldmap', 'par': 'up'},
        'down': {'url': 'worldmap', 'par': 'down'},
        'left': {'url': 'worldmap', 'par': 'left'},
        'right': {'url': 'worldmap', 'par': 'right'},
        'start': {'url': 'options'},
        'select': {'url': 'moviedex'},
        'a': {'url': 'battle', 'par': moviemon_id} if moviemon_id else None,
        'b': {'url': 'load_game'}
    }
    return Render(request, 'worldmap', {'settings': settings}, actions=actions)


def battle(request, moviemon_id, throw=None):
    def is_fight_sucess() -> bool:
        pass

    if throw:
        is_fight_sucess()

    actions = {
        'start': {'url': 'options'},
        'select': {'url': 'moviedex'},
        'a': {'url': 'battle', 'par': 1},
        'b': {'url': 'load_game'}
    }
    return Render(request, 'battle', actions=actions)


def moviedex(request, moviemon_id):
    actions = {
        'left': {'url': 'worldmap', 'par': 'left'},
        'right': {'url': 'worldmap', 'par': 'right'},
        'start': {'url': 'options'},
        'select': {'url': 'worldmap'},
        'a': {'url': 'moviedex', 'par': moviemon_id} if moviemon_id else None,
    }
    return Render(request, 'worldmap', {'settings': settings}, actions=actions)


def detail(request):
    pass


def options(request):
    # ’A - Save’, ’B - Quit’ as well as ’start - cancel’
    help_list = ['a: save', 'b: quit', 'start: cancel']
    actions = {
        'a': {'url': 'save_game'}
    }
    return Render(request, context={'help': help_list}, actions=actions).render()

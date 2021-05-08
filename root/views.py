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


def save_game(request, slot=0):
    def is_selected(i):
        return slot % 3 == i

    # ’Slot A’, ’Slot B’ and ’Slot C’
    slots = [{'text': 'slot a: 12/15', 'selected': is_selected(0)},
             {'text': 'slot b: 11/21', 'selected': is_selected(1)},
             {'text': 'slot c: free', 'selected': is_selected(2)}]
    help_list = ['a: save', 'b: cancel']
    return Render(request, 'save', context={'help': help_list, 'slots': slots, 'selected': slot % 3}).render()


def load_game(request, slot=0):
    def is_selected(i):
        return slot % 3 == i

    # ’Slot A’, ’Slot B’ and ’Slot C’
    slots = [{'text': 'slot a: 12/15', 'selected': is_selected(0)},
             {'text': 'slot b: 11/21', 'selected': is_selected(1)},
             {'text': 'slot c: free', 'selected': is_selected(2)}]
    help_list = ['a: save', 'b: cancel']
    actions = {'up': {'url': 'load_game', 'par': (slot + 1) % 3}, 'down': {'url': 'load_game', 'par': (slot - 1) % 3}}
    return Render(request, 'save', context={'help': help_list, 'slots': slots, 'selected': slot % 3},
                  actions=actions).render()


def moviemon(request):
    pass


def worldmap(request, new=''):
    default = Supplier.load_default_settings()
    max_x = default.get('grid_size_x')
    max_y = default.get('grid_size_y')
    player = default.get('start_x'), default.get('start_y')

    def is_player(n):
        return n % max_x == player[0] and n // max_y == player[1]

    def coin():
        return random.choice([True, False])

    # 'x': n % max_x, 'y': n // max_y,
    map_list = [{'player': is_player(n), 'ball': coin(), 'pokemon': coin()} for n in range(max_x * max_y)]
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
        # TODO: A: Only if a Moviemon is flushed out: Link to Battle page of the battle against this Moviemon.
        'a': {'url': 'battle', 'par': 1},
        'b': {'url': 'load_game'}
    }
    return Render(request, 'battle', actions=actions)


def moviedex(request):
    pass


def detail(request):
    pass


def options(request):
    # ’A - Save’, ’B - Quit’ as well as ’start - cancel’
    help_list = ['a: save', 'b: quit', 'start: cancel']
    return Render(request, context={'help': help_list}).render()

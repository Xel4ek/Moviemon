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
import copy
import random

from .classes import Map
from .models import Supplier
from .tools import Render


def index(request):
    help_list = ['a: new game', 'b: load']
    actions = {'a': {'url': 'worldmap', 'par': 'new'}, 'b': {'url': 'load_game', 'par': 0}}
    return Render(request, context={'help': help_list}, actions=actions).render()


def save_game(request, slot=0):
    magic = 123

    def is_selected(i):
        return slot % 3 == ord(i) - ord('a')

    if slot > 2 and 3 > slot - magic > 0:
        Supplier.dump(chr(ord('a') + slot - magic))
        slot -= magic

    slots = [{'text': 'slot ' + key + ':' + value, 'selected': is_selected(key)} for (key, value) in
             Supplier.info().items()]
    help_list = ['a: save', 'b: cancel']
    actions = {
        'up': {'url': 'save_game', 'par': (slot - 1) % 3}, 'down': {'url': 'save_game', 'par': (slot + 1) % 3},
        'a': {'url': 'save_game', 'par': slot + magic}, 'b': {'url': 'options'}}

    return Render(request, 'save', context={'help': help_list, 'slots': slots, 'selected': slot % 3},
                  actions=actions).render()


def load_game(request, slot=0):
    def is_selected(i):
        return slot % 3 == ord(i) - ord('a')

    def empty():
        return Supplier.info().get(chr(slot + ord('a'))) == 'free'

    slots = [{'text': 'slot ' + key + ':' + value, 'selected': is_selected(key)} for (key, value) in
             Supplier.info().items()]
    help_list = ['a: load', 'b: cancel']
    actions = {'up': {'url': 'load_game', 'par': (slot - 1) % 3}, 'down': {'url': 'load_game', 'par': (slot + 1) % 3},
               'a': {'url': 'worldmap', 'par': chr(slot + ord('a'))} if not empty() else None, 'b': {'url': 'index'}}
    return Render(request, 'save', context={'help': help_list, 'slots': slots, 'selected': slot % 3},
                  actions=actions).render()


def moviemon(request):
    pass


def worldmap(request, new=None):
    message = []
    moviemon_id = None
    default = Supplier.load_default_settings()
    directions = ['up', 'left', 'right', 'down']
    if new == 'new':
        Supplier.new_game()
    if new == 'a' or new == 'b' or new == 'c':
        Supplier.load(new)
    if new in directions:
        Supplier.game.move(new)
    map_list = copy.deepcopy(Supplier.game.map.items)
    context: Map.Cell = Supplier.game.context()
    if context.ball:
        Supplier.game.pick_ball()
        message = ['A movieball is found']
    if context.moviemon and not context.moviemon.caught:
        message = ['Moviemon flushed out', 'A: Battle']
        moviemon_id = context.moviemon.id
    if Supplier.game.count_caught_moviemons() == Supplier.game.count_moviemons():
        message = ['Congratulations!', 'Every moviemons was caught']
    possibility = Supplier.game.can_move
    settings = {**default, 'map_list': map_list, 'balls': Supplier.game.count_balls(),
                'message': message}
    # TODO: set moviemon_id on move
    actions = {
        **{direct: {'url': 'worldmap', 'par': direct} if possibility(direct) else None for direct in directions},
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
        'a': {'url': 'save_game'}, 'b': {'url': 'index'}, 'start': {'url': 'worldmap'}
    }
    return Render(request, context={'help': help_list}, actions=actions).render()

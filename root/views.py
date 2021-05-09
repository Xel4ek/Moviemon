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
import math

from .classes import Map, Moviemon
from .models import Supplier
from .tools import Render


def index(request):
    help_list = ['a: new game', 'b: load']
    actions = {'a': {'url': 'worldmap', 'par': 'new'}, 'b': {'url': 'load_game'}}
    return Render(request, context={'help': help_list}, actions=actions).render()


def save_game(request, slot=0):
    magic = 123

    def is_selected(i):
        return slot % 3 == ord(i) - ord('a')

    if slot > 2 and 3 > slot - magic >= 0:
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

    slots = [{'text': 'slot {}:{} '.format(key, value), 'selected': is_selected(key)} for (key, value) in
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
    default = Supplier.size()
    directions = ['up', 'left', 'right', 'down']
    if new == 'new':
        Supplier.new_game()
    if new == 'a' or new == 'b' or new == 'c':
        Supplier.load(new)
    if new in directions:
        Supplier.game().move(new)
    map_list = copy.deepcopy(Supplier.game().map.items)
    context: Map.Cell = Supplier.game().context()
    if context.ball:
        Supplier.game().pick_ball()
        message = ['A movieball is found']
    if context.moviemon and not context.moviemon.caught:
        message = ['Moviemon flushed out', 'A: Battle']
        moviemon_id = context.moviemon.id
    if Supplier.game().count_caught_moviemons() == Supplier.game().count_moviemons():
        message = ['Congratulations!', 'Every moviemons was caught']
    if Supplier.game().balls == 0 and Supplier.game().remaining_balls() == 0:
        message = ['Wasted!', 'You can continue the meaningless', 'existence, but the balls run out']
    possibility = Supplier.game().can_move
    settings = {**default, 'map_list': map_list, 'balls': Supplier.game().count_balls(),
                'message': message}
    actions = {
        **{direct: {'url': 'worldmap', 'par': direct} if possibility(direct) else None for direct in directions},
        'start': {'url': 'options'},
        'select': {'url': 'moviedex'} if 0 != Supplier.game().count_caught_moviemons() else None,
        'a': {'url': 'battle', 'par': moviemon_id} if moviemon_id else None,
    }
    return Render(request, 'worldmap', {'settings': settings}, actions=actions)


def battle(request, moviemon_id):
    fight = moviemon_id[-1] == '!'
    if fight and Supplier.game().count_balls():
        moviemon_id = moviemon_id.strip('!')
        Supplier.game().fight(moviemon_id)

    actions = {
        'start': {'url': 'options'},
        'select': {'url': 'moviedex'},
        'a': {'url': 'battle', 'par': moviemon_id + '!'} if Supplier.game().count_balls() and
                                                            not Supplier.game().status(moviemon_id).caught else None,
        'b': {'url': 'worldmap'}
    }

    moviemon = Supplier.game().moviemons.get(moviemon_id)

    massage = [None if not fight else 'You caught it!' if Supplier.game().status(moviemon_id).caught else 'you missed!',
               'your strength: {}'.format(Supplier.game().get_strength()),
               'you have {} ball(s)'.format(Supplier.game().count_balls()),
               'enemy strength {}'.format(moviemon.rating),
               'chance to win:{}%'.format(Supplier.game().chance(moviemon_id)),
               'A:Launch movieball']
    return Render(request, 'battle',
                  {'moviemon': moviemon, 'massage': massage}, actions=actions)


def moviedex(request, action=None):
    control = ['up', 'left', 'right', 'down']
    map_list = [item for item in Supplier.get_movie().values()]
    size = math.ceil(math.sqrt(Supplier.game().count_moviemons()))

    selected = Supplier.selected
    if action in control:
        selected = Map.move_map.get(action)(selected, size)
        if 0 <= selected < len(map_list):
            Supplier.selected = selected
    elif action != 'back':
        Supplier.selected = 0

    for item in map_list:
        item.selected = False
    if len(map_list) != 0:
        map_list.sort(key=lambda x: x.time, reverse=True)
        map_list[Supplier.selected].selected = True

    actions = {**{key: {'url': 'moviedex', 'par': key} for key in control},
               'start': {'url': 'options'},
               'select': {'url': 'worldmap'},
               'a': None if len(map_list) == 0 else {'url': 'detail', 'par': map_list[Supplier.selected].id},
               }
    settings = {'grid_size_x': size, 'grid_size_y': size, 'map_list': map_list}
    return Render(request, 'moviedex', {'settings': settings}, actions=actions)


def detail(request, moviemon_id):
    actions = {
        'b': {'url': 'moviedex', 'par': 'back'}
    }

    moviemon: Moviemon = Supplier.game().moviemons.get(moviemon_id)
    massage = [moviemon.name, 'by {}'.format(moviemon.director), 'at {}'.format(moviemon.year),
               'imdb: {}'.format(moviemon.rating), moviemon.synopsis, moviemon.actors, 'b:back']
    return Render(request, 'details',
                  {'moviemon': moviemon, 'massage': massage}, actions=actions)


def options(request):
    help_list = ['a: save', 'b: quit', 'start: cancel']
    actions = {
        'a': {'url': 'save_game'}, 'b': {'url': 'index'}, 'start': {'url': 'worldmap'}
    }
    return Render(request, context={'help': help_list}, actions=actions).render()

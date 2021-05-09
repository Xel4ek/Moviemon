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
from math import sqrt, ceil

from django.http import Http404

from .classes import Map, Game
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
        'select': {'url': 'moviedex'},
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

    massage = [ None if not fight else 'You caught it!' if Supplier.game().status(moviemon_id).caught else 'you missed!',
               'your strength: {}'.format(Supplier.game().get_strength()),
               'you have {} ball(s)'.format(Supplier.game().count_balls()),
               'enemy strength {}'.format(moviemon.rating),
               'chance to win:{}%'.format(Supplier.game().chance(moviemon_id)),
               'A:Launch movieball' if not moviemon.caught else '',
                'B: Back']
    return Render(request, 'battle',
                  {'moviemon': moviemon, 'massage': massage}, actions=actions)


def moviedex(request, moviemon_id=0):
    movies = Supplier.game().caught_moviemons()
    print(movies)
    actions = {
        'right': {'url': 'moviedex', 'par': moviemon_id + 1} if moviemon_id + 1 < len(movies) else None,
        'left': {'url': 'moviedex', 'par': moviemon_id - 1} if moviemon_id - 1 >= 0 else None,
        'a': {'url': 'detail', 'par': moviemon_id} if len(movies) > 0 else None,
        'b': {'url': 'options'}
    }
    return Render(request, 'moviedex',
                  {'movies': movies,
                   'selected': movies[moviemon_id] if movies else None,
                   'height': ceil(sqrt(538 * 450 / Supplier.game().count_moviemons() * 4 / 3)),
                   'empty': len(movies) == 0,
                   },
                  actions=actions)

def detail(request, idx=0):
    movies = Supplier.game().caught_moviemons()
    actions = {
        'b': {'url': 'moviedex'}
    }
    return Render(request, 'detail', {'movie': movies[idx]}, actions=actions)




def options(request):
    # ’A - Save’, ’B - Quit’ as well as ’start - cancel’
    help_list = ['a: save', 'b: quit', 'start: cancel']
    actions = {
        'a': {'url': 'save_game'}, 'b': {'url': 'index'}, 'start': {'url': 'worldmap'}
    }
    return Render(request, context={'help': help_list}, actions=actions).render()

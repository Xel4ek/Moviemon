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
    pass


def battle(request):
    pass


def moviedex(request):
    pass


def detail(request):
    pass


def options(request):
    pass

import random
import uuid

from django.utils.datetime_safe import datetime


class Map:
    """
        'position_x': 0,
        'position_y': 0,
    """

    move_map = {
        'up': lambda x, size: x - size,
        'down': lambda x, size: x + size,
        'left': lambda x, size: x - 1,
        'right': lambda x, size: x + 1
    }

    class Cell:

        def __init__(self, player=False, moviemon=None, ball=False):
            self.player = player
            self.moviemon = moviemon
            self.ball = ball

    def __init__(self, size):
        self.size = size
        self.items = [Map.Cell() for i in range(self.size[0] * self.size[1])]

    def get_size(self):
        return self.size

    def cell_content(self, x, y):
        if x > self.size[0] or y > self.size[1] or x < 0 or y < 0:
            raise IndexError()
        return self.items[y * self.size[1] + x]

    def get_position(self):
        for i in range(self.size[0] * self.size[1]):
            if self.items[i].player:
                return i
        raise Exception('No player')

    def can_move(self, direction):
        player_idx = self.get_position()
        target_idx = Map.move_map.get(direction)(player_idx, self.size[0])
        if target_idx < 0 or target_idx >= self.size[0] * self.size[1]:
            return False
        diff_x = player_idx % self.size[0] - target_idx % self.size[0]
        diff_y = player_idx // self.size[1] - target_idx // self.size[1]
        if diff_x != 0 and diff_y != 0:
            return False
        return True

    def move_player(self, direction):
        player_idx = self.get_position()
        self.items[player_idx].player = False
        player_idx = Map.move_map.get(direction)(player_idx, self.size[0])
        self.items[player_idx].player = True

    def set_cell(self, cell, idx):
        self.items[idx] = cell

    def pick_ball(self):
        player_idx = self.get_position()
        self.items[player_idx].ball = False

class Moviemon:

    def __init__(self, name, poster, director, year, rating, synopsis, actors):
        self.id = str(uuid.uuid4())
        self.poster = poster
        self.name = name
        self.director = director
        self.year = year
        self.rating = rating
        self.synopsis = synopsis
        self.actors = actors
        self.caught = False
        self.time = datetime.now()

    def catch(self):
        self.time = datetime.now()
        self.caught = True

    def strength(self):
        return self.rating

    @staticmethod
    def from_movie(movie):
        '''
        EXAMPLE
        "Title": "Dark", "Year": "2017–2020", "Rated": "TV-MA",
        "Released": "01 Dec 2017", "Runtime": "60 min",
        "Genre": "Crime, Drama, Mystery, Sci-Fi, Thriller", "Director": "N/A",
        "Writer": "Baran bo Odar, Jantje Friese",
        "Actors": "Louis Hofmann, Karoline Eichhorn, Lisa Vicari, Maja Schöne",
        "Plot": "A family saga with a supernatural twist, set in a German town, where the disappearance of two young children exposes the relationships among four families.",
        "Language": "German", "Country": "Germany, USA",
        "Awards": "6 wins & 20 nominations.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BOTk2NzUyOTctZDdlMS00MDJlLTgzNTEtNzQzYjFhNjA0YjBjXkEyXkFqcGdeQXVyMjg1NDcxNDE@._V1_SX300.jpg",
        "Ratings": [{"Source": "Internet Movie Database", "Value": "8.8/10"}],
        "Metascore": "N/A", "imdbRating": "8.8", "imdbVotes": "294,486",
        "imdbID": "tt5753856", "Type": "series", "totalSeasons": "3",
        "Response": "True"'''
        return Moviemon(movie.get('Title'), movie.get('Poster'), movie.get('Director'), movie.get('Released'),
                        float(movie.get('imdbRating')), movie.get('Plot'), movie.get('Actors'))


class Game:
    """
    'player': False,
    'pokemon': False,
    'ball': False,
    'visited': False,
    'balls': 0,
    'moviemons': {},
    'strength': 0,
    'map': Map(),
    'settings': {
        'start_x': 2,
        'start_y': 2,
        'map_x': 10,
        'map_y': 10,
        'low': 4,
        'high': 4,
    """
    class NoBallsException(Exception):
        def __init__(self):
            super().__init__("Muahaha! You've got no balls!")

    def __init__(self, moviemons, settings):
        self.moviemons = {}
        size = (settings.get('grid_size_x'), settings.get('grid_size_y'))
        self.map: Map = Map(size)
        for i in range(0, settings.get('max_balls')):
            self.map.items[i].ball = True
        for i in range(0, len(moviemons)):
            moviemon = moviemons[i]
            self.moviemons[moviemon.id] = moviemon
            self.map.items[i + settings.get('max_balls')].moviemon = self.moviemons[moviemon.id]
        random.shuffle(self.map.items)
        self.map.items[settings.get('start_x') + settings.get('start_y') * size[0]].player = True
        self.max_balls = settings.get('max_balls')
        self.balls = 0

    def get_map_size(self):
        return self.map.get_size()

    def caught_moviemons(self):
        return [filter(lambda x: x.caught, self.moviemons)]

    def count_caught_moviemons(self):
        return len([i for i in self.moviemons.values() if i.caught])

    def count_moviemons(self):
        return len(self.moviemons)

    def count_balls(self):
        return self.balls

    def get_strength(self):
        return self.count_caught_moviemons()

    def chance(self, moviemon):
        mov: Moviemon = self.moviemons.get(moviemon)
        return min(90, max(1, 50 - mov.strength() * 10 + self.get_strength() * 5))

    def fight(self, moviemon):
        if self.balls < 1:
            raise Game.NoBallsException()
        self.balls -= 1
        coin = random.random() * 100
        if coin < self.chance(moviemon):
            self.moviemons.get(moviemon).catch()

    def status(self, moviemon) -> Moviemon:
        return self.moviemons.get(moviemon)

    def pick_ball(self):
        self.balls += 1
        self.map.pick_ball()

    def info(self):
        return str(self.count_caught_moviemons()) + '/' + str(self.max_balls)

    def move(self, action):
        if self.can_move(action):
            return self.map.move_player(action)

    def can_move(self, direct):
        return self.map.can_move(direct)

    def context(self):
        return self.map.items[self.map.get_position()]

    def remaining_balls(self):
        return len([i for i in self.map.items if i.ball])


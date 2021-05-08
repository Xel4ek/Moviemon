import random
import uuid


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
    """

    class NoBallsException(Exception):
        raise Exception("Muahaha! You've got no balls!")

    def __init__(self, map, balls, moviemons):
        self.map: Map = map
        self.balls = balls
        self.moviemons = moviemons

    def get_map_size(self):
        return self.map.get_size()

    def count_caught_moviemons(self):
        return len([i for i in self.moviemons if i.caught])

    def count_moviemons(self):
        return len(self.moviemons)

    def count_balls(self):
        return self.balls

    def get_strength(self):
        return self.count_caught_moviemons()

    def fight(self, moviemon):
        if self.balls < 1:
            raise Game.NoBallsException()
        self.balls -= 1
        mov: Moviemon = self.moviemons.get(moviemon)
        c = min(90, max(1, 50 - mov.strength() * 10 + self.get_strength() * 5))
        coin = random.randint(0, 100)
        if coin < c:
            mov.catch()

    def pick_ball(self):
        self.balls += 1
        self.map.pick_ball()


class Moviemon:

    def __init__(self, name, poster, director, year, rating, synopsis, actors):
        self.id = uuid.uuid4()
        self.poster = poster
        self.name = name
        self.director = director
        self.year = year
        self.rating = rating
        self.synopsis = synopsis
        self.actors = actors
        self.caught = False

    def catch(self):
        self.caught = True

    def strength(self):
        return self.rating


class Map:
    """
        'position_x': 0,
        'position_y': 0,
    """

    _move_map = {
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
        self.items = [Map.Cell() for i in range(self.size * self.size)]

    def get_size(self):
        return self.size

    def cell_content(self, x, y):
        if x > self.size or y > self.size or x < 0 or y < 0:
            raise IndexError()
        return self.items[y * self.size + x]

    def get_position(self):
        for i in range(self.size * self.size):
            if self.items[i].player:
                return i

    def can_move(self, direction):
        player_idx = self.get_position()
        target_idx = Map._move_map.get(direction)(player_idx, self.size)
        if player_idx < 0 or player_idx > self.size * self.size:
            return False
        diff_x = player_idx % self.size - target_idx % self.size
        diff_y = player_idx // self.size - target_idx // self.size
        if diff_x == diff_y:
            return False
        return True

    def move_player(self, direction):
        player_idx = self.get_position()
        self.items[player_idx].player = False
        player_idx = Map._move_map.get(direction)(player_idx, self.size)
        self.items[player_idx].player = True

    def set_cell(self, cell, idx):
        self.items[idx] = cell

    def pick_ball(self):
        player_idx = self.get_position()
        self.items[player_idx].ball = False



